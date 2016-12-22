(function () {
    'use strict';

    var app = angular.module('participant-filter', []);


    app.filter('event_has_participant', function ($scope, $log) {
       return function (events, hasEvents) {



           hasEvents = false;

           angular.forEach(events, function (event) {

               var has_participant = false;

               angular.forEach(event.sessions, function (session) {

                   if(!has_participant) {
                       if(session.filterParticipant.length)
                       {
                           event.has_participant = true;
                           has_participant = true;
                       }
                   };

               });

               if(!has_participant)
               {
                   event.has_participant = false;
               }

               hasEvents = hasEvents || event.has_participant;
           });

           return events;
       };
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

                                if(keep_checking)
                                {
                                    if(new Date(occurrence.begin_date_time) <= searchCriteria)
                                    {
                                        filteredArray.push(event);
                                        keep_checking = false;
                                    }
                                }
                            });
                        };
                    });
                }


            });

            return filteredArray;
        };
    }]);
/*
    app.filter('event_category_filter', ['$log', function ($filter) {
        return function (originalArray, searchCriteria, EventLabel) {

            if(!angular.isDefined(searchCriteria) || searchCriteria == '' || searchCriteria == null || searchCriteria == ())
                return originalArray;

            console.log(searchCriteria);
            var filteredArray = [];

            angular.forEach(originalArray, function (event) {

                if(event.category.id == searchCriteria)
                    filteredArray.push(event);

            });

            return filteredArray;
        };
    }]);
*/
})(window.angular);