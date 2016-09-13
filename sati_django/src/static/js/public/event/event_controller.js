(function () {
    'use strict';

    var app = angular.module('event-controller', ['event-directive']);

    app.controller('EventCtrl', function EventCtrl($scope, $log, $http, ModelUtils,
                                                   Urls) {

        var eventCtrl = this;
        eventCtrl.events = [];

        this.loadEvents = function () {
            var promise = ModelUtils.get_all(Urls.event());

            promise.then(function (response) { // Success
                //$log.log('event');
                angular.forEach(response.results, function (event) {
                    //$log.log(event);
                    eventCtrl.events.push(event);
                });

            }, function (result) { // Fail
                $log.log('error');
                $log.log(value.status + ' ' + value.statusText);
            });
        };

        this.loadEvents();


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