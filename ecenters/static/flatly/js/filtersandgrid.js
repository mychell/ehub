/**
 * Code for the filters and grid overlay.
 *
 * It's sort of modular in the sense that we use it on the venue detail and venue search pages, but it's also extremely
 * tightly couple and some of this stuff will have to be factored out at some point.
 *
 */
var filtersAndGrid = (function() {
    var profileInfo,
        PENDING_QUOTE_REQUEST_TXT = "PENDING QUOTE REQUEST";

    // using jQuery (from django docs...TODO move this someplace else)
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    /**
     * Return the index of the the first item in `values` that `value` is greater than.
     */
    function firstIndex(values, value) {
        value = parseInt(value);
        if (value != undefined && !isNaN(value)) {
            for (var i=values.length - 1; i>=0; i--) {
                if (value >= values[i]) {
                    return i;
                }
            }
            return -1;
        }
    }

    function disablePendingQuoteRequestButtons() {
        if (profileInfo) {  // profile info shouldn't really ever be undefined when this method is called, but for some reason it seems to get into that state in firefox.
            for (var venue_id in profileInfo.booked_venues) {
                var button = $("a.get-quote-btn[data-venue-id='" + venue_id + "']");

                button.toggleClass("disabled", true);
                button.html(PENDING_QUOTE_REQUEST_TXT);
            }
        }
    }

    function getProfileInfo() {
        $.get('/profiles/info/')
            .done(function(data) {
                profileInfo = data;
                disablePendingQuoteRequestButtons();
            })
            .fail(function() {
                //Could not get profile info, the user is either not logged in or the session has expired
            });
    }

    function createBooking(event_id, venue_id, button) {
        button.toggleClass("disabled", true);
        var data = {
            event_id: event_id,
            venue_id: venue_id,
            csrftoken: getCookie('csrftoken')
        };
        $.post('/booking/create-ajax/', data)
            .done(function() {
                button.html(PENDING_QUOTE_REQUEST_TXT);
                profileInfo.booked_venues[venue_id] = true;
                ga('send', 'event', 'quote_request', 'click', 'grid button', venue_id);
            })
            .fail(function() {
                alert('Sorry, something went wrong submitting your quote request. Please try again later.');
            });
    }

    function gridOverlay(userLoggedIn) {
        /* quote/more info overlay's on search grid */
        $(".similar-overlay").hide();
        $(document).on("mouseenter", ".img-container", function() {
            $(this).find(".similar-overlay").fadeIn();
        });
        $(document).on("mouseleave", ".img-container", function() {
            $(this).find(".similar-overlay").fadeOut();
        });

        if (userLoggedIn) {
            getProfileInfo();
        }

        $(document).on("click", "a.get-quote-btn", function(e) {
            var button = $(this);

            if (button.data("clicked") == "true" || button.hasClass('disabled')) {
                e.preventDefault();
                return;
            }

            if (userLoggedIn && profileInfo && profileInfo.events.length == 1) {
                button.data("clicked", "true");

                createBooking(profileInfo.events[0].id, button.data('venue-id'), button);
                e.preventDefault();

            } else if (userLoggedIn && profileInfo && profileInfo.events.length > 1) {
                button.data("clicked", "true");

                //pop modal, pick event(s), create booking
                var template = $('#multipleEventsTemplate').html();
                $('#multipleEventsModal-inner').html(Mustache.render(template, profileInfo));

                $('#multipleEventsSubmit').click(function() {
                    $('#multipleEventsModal-inner input:checked').each(function(index, element){
                        createBooking($(element).data('event-id'), button.data('venue-id'), button);
                    });
                    $('#multipleEventsModal').modal('hide');
                });

                $('#multipleEventsModal').modal('show');
                e.preventDefault();
            }
        });
    }

    function dataFromForm() {
       var budget = undefined;
        if ($("#budget-null:checked").length == 0) {
            budget = $("#budget").val().replace(/\$|\,|\+/g, "");
        }

        var occupancy = undefined;
        if ($("#occupancy-null:checked").length == 0) {
            occupancy = $("#occupancy").val().replace(/\$|\,|\+/g, "");
        }

        var data = {
            seed: $("#seed").val(),
            page: $('#page').val(),
            budget: budget,
            occupancy: occupancy,
            neighborhood: $('#neighborhood').val() ? $('#neighborhood').val().join(",") : undefined,
            venue_type: $('#venue_type').val() ? $('#venue_type').val().join(",") : undefined,
            amenity: $('#amenity').val() ? $('#amenity').val().join(",") : undefined,
            event_type: $('#event_type').val() ? $('#event_type').val().join(",") : undefined
        };

        if ($("#lat_lng").val()) {
            data.lat_lng = $("#lat_lng").val();
        }

        if ($("#city_slug").val()) {
            data.city_slug = $("#city_slug").val();
        }

        if ($("#query_str").val()) {
            data.query_str = $("#query_str").val();
        }

        if ($("#raw_query_str").val()) {
            data.raw_query_str = $("#raw_query_str").val();
        }

        return data;
    }

    function dataToForm(data) {

        if (data.reset) {
            return;
        }

        $("#lat_lng").val(data.lat_lng);
        $("#city_slug").val(data.city_slug);
        $("#query_str").val(data.query_str);
        $("#raw_query_str").val(data.raw_query_str);
        $("#seed").val(data.seed);
        $('#page').val(data.page);

        if (data.budget != undefined) {
            $("#budget").val("$" + parseInt(data.budget).toLocaleString());
        }

        if (data.occupancy != undefined) {
            $("#occupancy").val(parseInt(data.occupancy).toLocaleString());
        }

        $('#neighborhood').val(data.neighborhood ? data.neighborhood.split(",") : undefined);
        $('#venue_type').val(data.venue_type ? data.venue_type.split(",") : undefined);
        $('#amenity').val(data.amenity ? data.amenity.split(",") : undefined);
        $('#event_type').val(data.event_type ? data.event_type.split(",") : undefined);
    }

    function filterChanged(resetPage) {
        $("#gridContent").html("<h1>Loading...</h1>");
        $('#prev-button').toggleClass("disabled", true);
        $('#next-button').toggleClass("disabled", true);

        if (resetPage) {
            $('#page').val(1);
        }

        var data = dataFromForm();

        if (Modernizr.history) {
            history.replaceState(data, "search", window.location);
        }

        var page = window.location.pathname + "?" + jQuery.param(data);
        ga('send', 'pageview', page);

        $.get('/search/ajax/', data)
            .done(function(data) {
                if (data.data.length > 0) {
                    $('#gridContent').html(data.data.join(""));
                    $(".similar-overlay").hide();

                    $('#prev-button').toggleClass("disabled", !data.has_prev);
                    $('#next-button').toggleClass("disabled", !data.has_next);

                    $('#results-count').html(data.count + " results");
                } else {
                    $('#gridContent').html("<h1>Sorry!</h1><p>We can't find any venues matching your search criteria. Try broadening them up, and we'll see what we can find.</p>");
                    $('#prev-button').toggleClass("disabled", true);
                    $('#next-button').toggleClass("disabled", true);

                    $('#results-count').html(data.count + " results");
                }

                disablePendingQuoteRequestButtons();
            })
            .statusCode({
                404: function() {
                    if (Modernizr.history) {
                        history.replaceState({reset: true}, "search", window.location);
                    }

                    $('#gridContent').html(
                        "<h2>Sorry, that's all we've got.</h2>" +
                        '<div class="paginationButtons">' +
                        '<p><a href="' + window.location.href + '" type="button" class="btn" id="prev-button">Go Back to the Start</a></p></div>');
                },
                500: function() {
                    if (Modernizr.history) {
                        history.replaceState({reset: true}, "search", window.location);
                    }

                    $('#gridContent').html('<h2>Oops, something went wrong!</h2> <p>We\'re working to resolve the problem.</p>' +
                        '<div class="paginationButtons">' +
                        '<p><a href="' + window.location.href + '" type="button" class="btn" id="prev-button">Try Again</a></p></div>');
                }
            });
    }

    function setupFilters() {
        if (Modernizr.history && history.state) {
            dataToForm(history.state);
        }

        /* filter change event for the drop down (chosen) search filters */
        $('.moreFilterSelect select').chosen().change(function() {
            filterChanged(true);
        });

        /* budget slider and its filter change event triggers */
        var prices = [250, 350, 450, 500, 750, 1000, 1250, 1500, 1750, 2000,
                      2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4500, 5000,
                      6000, 7000, 8000, 9000, 10000, 12000, 15000, 20000, 30000, 50000];
        $("#slider-price-range").slider({
            range: 'min',
            min: 0,
            max: 29,
            value: firstIndex(prices, $("#budget").val().replace(/\$|\,|\+/g, "")),
            slide: function(event, ui) {
                var actualValue = prices[ui.value];
                var postfix;
                if (ui.value == 29) {
                    postfix = "+";
                } else {
                    postfix = "";
                }
                $("#budget").val(("$" + actualValue.toLocaleString() + postfix));
            }
        }).on("slidestop", function() {
            $("#budget-null").attr("checked", false);
            filterChanged(true);
        });

        $("#budget-null").click(function() {
            $("#budget").val("");
            $("#slider-price-range").slider("value", 0);
            filterChanged(true);
        });

        /* attendance slider and its filter change event triggers */
        var occupancies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
                           60, 70, 80, 90, 100, 125, 150, 175, 200, 250,
                           300, 350, 400, 500, 750, 1000, 1500, 2000, 3000, 4000];
        $("#slider-occupancy-range").slider({
            range: 'min',
            min: 0,
            max: 29,
            value: firstIndex(occupancies, $('#occupancy').val().replace(/\$|\,|\+/g, "")),
            slide: function(event, ui) {
                var actualValue = occupancies[ui.value];
                var postfix;
                if (ui.value == 29) {
                    postfix = "+";
                } else {
                    postfix = "";
                }
                $("#occupancy").val(actualValue.toLocaleString() + postfix);
            }
        }).on("slidestop", function() {
            $("#occupancy-null").attr("checked", false);
            filterChanged(true);
        });

        $("#occupancy-null").click(function() {
            $("#occupancy").val("");
            $("#slider-occupancy-range").slider("value", 0);
            filterChanged(true);
        });

        /* show/hide filters button */
        $('#hideFilters').click(function() {
            $('.venue-filter').slideToggle();
            $('.venue-filter').removeClass('hide');
            $('.venue-filter').removeClass('vis-hidden');
            $(this).text(function(i, text){
                return text === "HIDE FILTERS" ? "SHOW FILTERS" : "HIDE FILTERS";
            });
        });

        /* search pagination buttons */
        $('#prev-button').click(function () {
            $('#page').val(parseInt($('#page').val(), 10) - 1);
            filterChanged(false);
        });

        $('#next-button').click(function() {
            $('#page').val(parseInt($('#page').val(), 10) + 1);
            filterChanged(false);
        });

        if (Modernizr.history && history.state) {
            filterChanged();
        }
    }

    //exports
    return {
        setupFilters: setupFilters,
        gridOverlay: gridOverlay
    }
})();
