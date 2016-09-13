(function () {
    'use strict';

    var app = angular.module('event-controller', ['event-directive']);

    app.controller('EventCtrl', function EventCtrl($scope, $log, $http, ModelUtils,
                                                   Urls) {

        var eventCtrl = this;
        eventCtrl.events = [];
        var promise;


        eventCtrl.loadEvents = function () {
            var promise = ModelUtils.get_all(Urls.event());

            promise.then(function (response) { // Success
                //$log.log('event');
                angular.forEach(response.results, function (event) {
                    //$log.log(event);
                    eventCtrl.events.push(event);
                });

            }, function (result) { // Fail
                $log.log('error');
                $log.log(result.status + ' ' + result.statusText);
            });
        };

        eventCtrl.loadEvents();

        eventCtrl.getPromise = function (promise) {

            var result;

            promise.then(function (response) { // Success

                $log.log(response);
                result = response;
                eventCtrl.tempPromise = response;

                /**
                    $scope.tempPromise = [];
                    angular.forEach(response.results, function (item) {
                        items.push(item);
                        console.log(JSON.stringify([item]));
                    });

                    $log.log(eventCtrl.tempPromise);
                 */

            }, function (result) { // Fail
                $log.log('error');
                $log.log(result.status + ' ' + result.statusText);
                result = result.status + ' ' + result.statusText;
            });

            return result;
        };

        eventCtrl.getEventRelation = function (event) {



        };
    });

})(window.angular);