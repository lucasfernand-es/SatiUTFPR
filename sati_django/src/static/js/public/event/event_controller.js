(function () {
    'use strict';

    var app = angular.module('event-controller',
        ['event-directive', 'event-factory', 'event-filter','ngMaterial']);

    var hasEvents = false;

    app.controller('EventDetailCtrl', function EventDetailCtrl($scope, $log, $http,
                                                               ModelUtils, Urls, Toast, Label,
                                                               EventLabel, EventUrls) {
        var eventDetail = this;
        eventDetail.event_id = $scope.event_id;

        // Factories
        eventDetail.EventLabel = EventLabel;
        eventDetail.Label = Label;

        eventDetail.loadEvent = function () {

            var promiseEvent = ModelUtils.get(Urls.event(), eventDetail.event_id);

            promiseEvent.then(function (response) { // Success
                eventDetail.event = response;

                var promiseEdition  = ModelUtils.get(Urls.edition(), eventDetail.event.edition);

                promiseEdition.then(function (response) {
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

                    var promiseSpotsSession = ModelUtils.get_request(EventUrls.spots_session_available(session.id));
                    promiseSpotsSession.then(function (response) {
                        session.spots_available = response.available_spots;
                        session.has_spots = response.available_spots > 0;

                    }, function (result) { // Fail
                        $log.log('error');
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