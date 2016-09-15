(function () {
    'use strict';

    var app = angular.module('event-controller',
        ['event-directive', 'event-factory', 'ngMaterial']);

    var hasEvents = false;


    app.controller('EventCtrl', function EventCtrl($scope, $log, $http,
                                                   ModelUtils, Urls,
                                                   Label,
                                                   EventLabel,
                                                   Toast) {
        var eventCtrl = this;

        eventCtrl.hasEvents = hasEvents;
        // Factories
        eventCtrl.EventLabel = EventLabel;
        eventCtrl.Label = Label;

        eventCtrl.events = [];

        $scope.message = Label.no_results();


        eventCtrl.loadEvents = function () {
            var promise = ModelUtils.get_all(Urls.event());

            promise.then(function (response) { // Success
                //$log.log('event');
                angular.forEach(response.results, function (event) {
                    //$log.log(event);
                    eventCtrl.events.push(event);


                });

            }, function (result) { // Fail
                Toast.showToast(result.status + ' ' + result.statusText);
            });
        };

        eventCtrl.loadEvents();

    });

    app.controller('EventDetailCtrl', function EventDetailCtrl($scope, $log, $http,
                                                               ModelUtils, Urls, Toast) {

        var eventDetail = this;
        eventDetail.current_event_id = $scope.current_event_id;
        //$log.log($scope.current_event_id);

        eventDetail.loadEvent = function () {

            var promiseEvent = ModelUtils.get(Urls.event(), eventDetail.current_event_id);

            promiseEvent.then(function (response) { // Success
                //$log.log(response);
                eventDetail.current_event = response;

                var promiseEdition  = ModelUtils.get(Urls.edition(), eventDetail.current_event.edition);

                promiseEdition.then(function (response) {
                        //$log.log(response);
                        eventDetail.current_event.edition = response;
                    }, function (result) {
                        Toast.showToast(result.status + ' ' + result.statusText);
                    });

                angular.forEach(eventDetail.current_event.sessions, function (session) {

                    //$log.log(session);

                    var promiseInstructor = ModelUtils.get(Urls.person(), session.instructor);
                    // get instructor
                    promiseInstructor.then(function (response) {
                        //$log.log(response);
                        session.instructor = response;
                    }, function (result) {
                        Toast.showToast(result.status + ' ' + result.statusText);
                    });

                    angular.forEach(session.occurrences, function (occurrence) {

                        var promiseRoom = ModelUtils.get(Urls.room(), occurrence.room);

                        promiseRoom.then(function (response) {
                            //$log.log(response);
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

    app.filter('event_begindate_filter', ['$log', function ($filter) {
        return function (originalArray, searchCriteria) {

            if(!angular.isDefined(searchCriteria) || searchCriteria == '' || searchCriteria == null)
                return originalArray;

            var filteredArray = [];

            angular.forEach(originalArray, function (event) {

                var sessions = event.sessions;
                var keep_checking = true;
                if(sessions.length > 0 && keep_checking)
                {
                    angular.forEach(sessions, function (session) {

                        var occurrences = session.occurrences;

                        if(occurrences.length > 0 && keep_checking)
                        {
                            angular.forEach(occurrences, function (occurrence) {
                                //console.log(occurrence);
                                //console.log(occurrence.begin_date_time);

                                if(keep_checking)
                                {
                                    if(new Date(occurrence.begin_date_time) <= searchCriteria)
                                    {
                                        filteredArray.push(event);
                                        keep_checking = false;
                                    }
                                    //console.log('searchCriteria');
                                    //console.log(searchCriteria);
                                }
                            });
                        };
                    });
                }


            });

            return filteredArray;
        };
    }]);
})(window.angular);