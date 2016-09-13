(function () {

    var app = angular.module('event-directive', []);

    app.directive('eventDetail', function(ModelUtils, Urls) {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/public/event/event_card.html',
            controller: function ($scope, $log) {
                $log.log($scope.event);

                var event = $scope.event;

                // reset
                $scope.current_event_session_ocurrence_room = '';

                var sessions = event.sessions;
                $scope.current_event_has_session = sessions.length > 0;

                if($scope.current_event_has_session) {
                    var occurrences = sessions[0].occurrences;
                    $scope.current_event_session_has_occurrence = occurrences.length > 0;

                    if($scope.current_event_session_has_occurrence)
                    {
                        $scope.current_event_session = sessions[0];
                        $scope.current_event_session_ocurrence = occurrences[0];

                        $log.log($scope.current_event_session);
                        $log.log($scope.current_event_session_ocurrence);

                        // person
                        promise = ModelUtils.get(Urls.person(), $scope.current_event_session.instructor);

                        promise.then(function (response) { // Success
                            $scope.current_event_session_instructor = response;
                        }, function (result) { // Fail
                            $log.log('error');
                            $log.log(result.status + ' ' + result.statusText);
                        });

                        promise = ModelUtils.get(Urls.room(), $scope.current_event_session_ocurrence.room);

                        promise.then(function (response) { // Success
                            $scope.current_event_session_ocurrence_room = response;
                        }, function (result) { // Fail
                            $log.log('error');
                            $log.log(result.status + ' ' + result.statusText);
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
