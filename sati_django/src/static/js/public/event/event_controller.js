(function () {
    'use strict';

    var app = angular.module('event-controller',
        ['event-directive', 'event-factory', 'event-filter','ngMaterial']);

    var hasEvents = false;


    app.controller('EventCtrl', function EventCtrl($scope, $log, $http,
                                                   ModelUtils, Urls,
                                                   Label,
                                                   EventLabel, EventUrls,
                                                   Toast) {
        var eventCtrl = this;

        eventCtrl.hasEvents = hasEvents;
        // Factories
        eventCtrl.EventLabel = EventLabel;
        eventCtrl.Label = Label;

        eventCtrl.events = [];
        eventCtrl.categories = [];

        $scope.message = Label.no_results();


        eventCtrl.loadEvents = function () {
            var promise = ModelUtils.get_all(Urls.event());

            promise.then(function (response) { // Success
                //$log.log('event');
                angular.forEach(response.results, function (event) {

                    var promiseCategory = ModelUtils.get(Urls.category(), event.category);

                    promiseCategory.then(function (response) { // Success
                        event.category = response;
                    }, function (result) { // Fail
                        $log.log('error');
                        Toast.showToast(result.status + ' ' + result.statusText);
                    });

                    var promiseSpotsEvent = ModelUtils.get_request(EventUrls.spots_event(event.id));

                    promiseSpotsEvent.then(function (response) {
                        $log.log(response);
                    }, function (result) { // Fail
                        $log.log('error');
                        Toast.showToast(result.status + ' ' + result.statusText);
                    })

                    //$log.log(event);
                    eventCtrl.events.push(event);


                });

            }, function (result) { // Fail
                Toast.showToast(result.status + ' ' + result.statusText);
            });
        };

        eventCtrl.loadCategories = function () {
            var promise = ModelUtils.get_all(Urls.category());

            promise.then(function (response) { // Success
                //$log.log('event');
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

    });

    app.controller('EventDetailCtrl', function EventDetailCtrl($scope, $log, $http,
                                                               ModelUtils, Urls, Toast,
                                                               Label, EventLabel) {

        var eventDetail = this;
        eventDetail.event_id = $scope.event_id;
        //$log.log($scope.event_id);

        // Factories
        eventDetail.EventLabel = EventLabel;
        eventDetail.Label = Label;

        eventDetail.loadEvent = function () {

            var promiseEvent = ModelUtils.get(Urls.event(), eventDetail.event_id);

            promiseEvent.then(function (response) { // Success
                //$log.log(response);
                eventDetail.event = response;

                var promiseEdition  = ModelUtils.get(Urls.edition(), eventDetail.event.edition);

                promiseEdition.then(function (response) {
                        //$log.log(response);
                        eventDetail.event.edition = response;
                    }, function (result) {
                        Toast.showToast(result.status + ' ' + result.statusText);
                    });

                var promiseCategory = ModelUtils.get(Urls.category(), eventDetail.event.category);

                    promiseCategory.then(function (response) { // Success
                        eventDetail.event.category = response;
                    }, function (result) { // Fail
                        $log.log('error');
                        Toast.showToast(result.status + ' ' + result.statusText);
                    });

                angular.forEach(eventDetail.event.sessions, function (session) {

                    var promiseInstructor = ModelUtils.get(Urls.person(), session.instructor);
                    // get instructor
                    promiseInstructor.then(function (response) {
                        session.instructor = response;
                    }, function (result) {
                        Toast.showToast(result.status + ' ' + result.statusText);
                    });

                    angular.forEach(session.occurrences, function (occurrence) {

                        var promiseRoom = ModelUtils.get(Urls.room(), occurrence.room);

                        promiseRoom.then(function (response) {
                            occurrence.room = response;

                        }, function (result) {
                            Toast.showToast(result.status + ' ' + result.statusText);
                        });

                    });


                });


            }, function (result) { // Fail
                Toast.showToast(result.status + ' ' + result.statusText);
            });

        };

        eventDetail.loadEvent();

    });

})(window.angular);