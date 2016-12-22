(function () {

    var app = angular.module('public-directive', []);

    app.directive('occurrenceInfo', function(ModelUtils, Urls) {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/public/occurrence_card.html',

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
