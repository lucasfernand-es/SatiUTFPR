(function () {
    'use strict';

    var app = angular.module('event-controller', []);

    app.controller('EventCtrl', function EventCtrl($scope, $log, $http, ModelUtils) {

        var eventCtrl = this;
        $scope.events = [];

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


        $scope.loadEvents();

        //$log.log("eventCtrl");
        //$log.log(eventCtrl.events);
    });

})(window.angular);