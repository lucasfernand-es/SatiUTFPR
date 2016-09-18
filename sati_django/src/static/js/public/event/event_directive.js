(function () {

    var app = angular.module('event-directive', []);

    app.directive('eventList', function() {
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
                $scope.EventLabel = EventLabel;
                $scope.Label = Label;
                eventCtrl.filteredEvents = [1];

                eventCtrl.categories = [];

                var promise;


                eventCtrl.loadEvents = function () {
                    eventCtrl.events = [];

                    promise = ModelUtils.get_request(Urls.get_all_events())
                        .then(function (response) {
                            angular.forEach(response, function (event) {

                                var keep_checking = true;
                                angular.forEach(event.sessions, function (session) {
                                    if(keep_checking) {

                                        angular.forEach(session.occurrences, function (occurrence) {
                                            if(keep_checking) {
                                                session.occurrence = occurrence;
                                                event.session = session;
                                                keep_checking = false;
                                            };
                                        });
                                    };
                                });

                                eventCtrl.events.push(event);
                            });
                        }, function (response) { // Fail
                                $log.log('error');
                                Toast.showToast(response.status + ' ' + response.statusText);
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
                    $scope.filter = {};
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
