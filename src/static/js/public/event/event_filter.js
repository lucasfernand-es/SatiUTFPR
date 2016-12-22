(function () {
    'use strict';

    var app = angular.module('event-filter', []);

    app.filter('event_begin_date_filter', function ($filter) {
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
                                    var occurrenceDate = new Date(occurrence.begin_date_time);

                                    var date = new Date(occurrenceDate.getUTCFullYear(),
                                         occurrenceDate.getUTCMonth(),
                                         occurrenceDate.getUTCDate());
                                    if(date <= searchCriteria)
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
    });

})(window.angular);