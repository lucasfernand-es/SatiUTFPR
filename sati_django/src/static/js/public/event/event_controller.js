(function () {
    'use strict';

    var app = angular.module('event-controller',
        ['event-directive', 'event-factory']);

    var hasEvents = false;

    app.controller('EventCtrl', function EventCtrl($scope, $log, $http,
                                                   ModelUtils, Urls,
                                                   Label,
                                                   Toast) {


        var eventCtrl = this;

        eventCtrl.hasEvents = hasEvents;
        // Factories
        eventCtrl.Label = Label;

        eventCtrl.events = [];


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