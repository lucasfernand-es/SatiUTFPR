(function () {

    var app = angular.module('event-directive', []);

    app.directive('eventList', function(ModelUtils, Urls) {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/public/event/event_list.html',
            controllerAs: 'eventCtrl',
            controller: function ($scope, $log, $http,
                                       ModelUtils, Urls,
                                       Label,
                                       EventLabel, EventUrls,
                                       Toast) {
                var eventCtrl = this;

                // Factories
                eventCtrl.EventLabel = EventLabel;
                eventCtrl.Label = Label;

                eventCtrl.events = [];
                eventCtrl.categories = [];

                $scope.message = Label.no_results();

                var promise;


                eventCtrl.loadEvents = function () {
                    var promise = ModelUtils.get_all(Urls.event());

                    promise.then(function (response) { // Success
                        angular.forEach(response.results, function (event) {

                            promise = ModelUtils.get(Urls.category(), event.category);

                            promise.then(function (response) { // Success
                                event.category = response;
                            }, function (result) { // Fail
                                $log.log('error');
                                Toast.showToast(result.status + ' ' + result.statusText);
                            });

                            var keep_checking = true;

                            angular.forEach(event.sessions, function (session) {
                                if(keep_checking)
                                {
                                    event.session = session;

                                    promise = ModelUtils.get(Urls.person(), session.instructor);
                                    promise.then(function (response) { // Success
                                        event.session.instructor = response;
                                    }, function (result) { // Fail
                                        $log.log('error');
                                        Toast.showToast(result.status + ' ' + result.statusText);
                                    });

                                    angular.forEach(session.occurrences, function (occurrence) {

                                        if(keep_checking){

                                            event.session.occurrence = occurrence;

                                            promise = ModelUtils.get(Urls.room(), occurrence.room);
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

                            var promiseSpotsEvent = ModelUtils.get_request(EventUrls.spots_event_available(event.id));
                            promiseSpotsEvent.then(function (response) {

                                event.has_spots = response.available_spots > 0;
                                event.has_session = !response.error;

                            }, function (result) { // Fail
                                $log.log('error');
                                Toast.showToast(result.status + ' ' + result.statusText);
                            });


                            eventCtrl.events.push(event);


                        });

                    }, function (result) { // Fail
                        Toast.showToast(result.status + ' ' + result.statusText);
                    });
                };

                eventCtrl.loadCategories = function () {
                    var promise = ModelUtils.get_all(Urls.category());

                    promise.then(function (response) { // Success

                        angular.forEach(response.results, function (item) {

                            eventCtrl.categories.push(item);

                        });

                    }, function (result) { // Fail
                        Toast.showToast(result.status + ' ' + result.statusText);
                    });

                };

                eventCtrl.loadEvents();
                eventCtrl.loadCategories();

                eventCtrl.clearFilter = function () {
                    $scope.search = '';
                    $scope.filter.begin_date = null;
                };

            },
        };
    });

    app.directive('eventDetail', function(ModelUtils, Urls) {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/public/event/event_card.html',
            controller: function ($scope, $log, Toast) {
                var event = $scope.event;
                //$log.log(event);
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
