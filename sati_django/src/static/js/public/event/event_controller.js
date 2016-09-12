(function () {
    'use strict';

    var app = angular.module('event-controller', []);

    app.controller('EventCtrl', function EventCtrl($scope, $log, $http, ModelUtils,
                                                   Urls) {

        var eventCtrl = this;
        $scope.events = [];
        $scope.events = ModelUtils.get_all(Urls.event());
        $scope.sessions = ModelUtils.get_all(Urls.session());

        $log.log('$scope');
        $log.log($scope.events);


        $scope.events.then(function (value) {
            $log.log('event');
            angular.forEach(value.results, function (event) {
                    $log.log(event);
                });
        }, function(value) {
            $log.log('error');
            $log.log(value.status + ' ' + value.statusText);
        });

        $scope.sessions.then(function (value) {
            $log.log('session');
            angular.forEach(value.results, function (item) {
                    $log.log(item);
                });
        }, function(value) {
            $log.log('error');
            $log.log(value.status + ' ' + value.statusText);
        });


        /*
        $scope.loadEvents = function () {
            $http.get('/api/event/').then(function (response) {
                $log.log(response.data.results);

                $scope.events = [];
                angular.forEach(response.data.results, function (event) {

                    $log.log(event);
                    $scope.events.push(event);
                });

                // return response.data.results;
            });
        };
        */


        //$scope.loadEvents();

        //$log.log("eventCtrl");
        //$log.log(eventCtrl.events);
    });

})(window.angular);