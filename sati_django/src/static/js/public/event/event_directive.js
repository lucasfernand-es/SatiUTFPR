(function () {

    var app = angular.module('event-directive', []);

    app.directive('eventDetail', function(ModelUtils, Urls) {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/public/event/event_card.html',
            controller: function ($scope, $log, Toast) {
                var event = $scope.event;

                var sessions = event.sessions;
                var keep_checking = true;

                var promise;
                event.has_session = false;

                angular.forEach(sessions, function (session) {

                    if(keep_checking) {

                        event.session = session;

                        // person
                        promise = ModelUtils.get(Urls.person(), event.session.instructor);
                        promise.then(function (response) { // Success
                            event.session.instructor = response;

                            $log.log(event);
                        }, function (result) { // Fail
                            $log.log('error');
                            Toast.showToast(result.status + ' ' + result.statusText);
                        });

                        angular.forEach(session.occurrences, function (occurrence) {

                            if(keep_checking){

                                event.session.occurrence = occurrence;

                                promise = ModelUtils.get(Urls.room(), event.session.occurrence.room);
                                promise.then(function (response) { // Success
                                    event.session.occurrence.room = response;
                                }, function (result) { // Fail
                                    $log.log('error');
                                    Toast.showToast(result.status + ' ' + result.statusText);
                                });

                                keep_checking = false;

                            };

                        });

                    };
                });
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
