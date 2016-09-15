(function () {
    'use strict';

    var app = angular.module('event-filter', []);

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