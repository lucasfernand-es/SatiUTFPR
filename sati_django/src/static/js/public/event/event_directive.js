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

    app.directive('sessionDetail', function(ModelUtils, Urls) {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/public/event/session_card.html',
            controller: function ($scope, $log, Toast) {
            },
        };
    });

    app.directive('occurrenceDetail', function(ModelUtils, Urls) {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/public/event/occurrence_card.html',
            controller: function ($scope, $log, Toast) {

                $log.log($scope.occurrence);

                var occurrence = $scope.occurrence;

                var begin_date_time = new Date(occurrence.begin_date_time);
                var end_date_time = new Date(occurrence.end_date_time);

                //$log.log(begin_date_time);
                //$log.log(end_date_time);


                var begin_date = new Date(
                    begin_date_time.getUTCFullYear(),
                    begin_date_time.getMonth(),
                    begin_date_time.getUTCDate()
                );

                var end_date = new Date(
                    end_date_time.getFullYear(),
                    end_date_time.getMonth(),
                    end_date_time.getUTCDate()
                );

                occurrence.is_same_day = !(begin_date < end_date);
                //$log.log(occurrence.is_same_day);


            },
        };
    });

})();
