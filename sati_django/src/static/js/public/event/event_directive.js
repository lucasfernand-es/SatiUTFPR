(function () {

    var app = angular.module('event-directive', []);

    app.directive('eventDetail', function(ModelUtils, Urls) {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/public/event/event_card.html',
            controller: function ($scope, $log, Toast) {
                var event = $scope.event;

                // reset
                event.current_event_session_ocurrence_room = '';

                var sessions = event.sessions;
                event.current_event_has_session = sessions.length > 0;

                if(event.current_event_has_session) {
                    event.current_event_session = sessions[0];

                    var occurrences = sessions[0].occurrences;
                    event.current_event_session_has_occurrence = occurrences.length > 0;

                    // person
                    promise = ModelUtils.get(Urls.person(), event.current_event_session.instructor);

                    promise.then(function (response) { // Success
                        event.current_event_session_instructor = response;
                    }, function (result) { // Fail
                        $log.log('error');
                        Toast.showToast(result.status + ' ' + result.statusText);
                    });


                    if(event.current_event_session_has_occurrence)
                    {

                        event.current_event_session_ocurrence = occurrences[0];



                        promise = ModelUtils.get(Urls.room(), event.current_event_session_ocurrence.room);

                        promise.then(function (response) { // Success
                            event.current_event_session_ocurrence_room = response;
                        }, function (result) { // Fail
                            $log.log('error');
                            Toast.showToast(result.status + ' ' + result.statusText);
                        });



                    }

                }
            },
        };
    });
/*
    app.directive("productDescriptions", function() {
        return {
          restrict: 'E',
          templateUrl: "../html/product-descriptions.html"
        };
    });
*/
})();
