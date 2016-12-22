(function () {
    'use strict';

    var app = angular.module('event-controller',
        ['event-directive', 'event-factory', 'event-filter','ngMaterial']);

    var hasEvents = false;

    app.controller('EventDetailCtrl', function EventDetailCtrl($scope, $log, $http,
                                                               ModelUtils, Urls, Toast, Label,
                                                               EventLabel) {
        var eventDetail = this;
        eventDetail.event_id = $scope.event_id;

        var promise;

        // Factories
        $scope.EventLabel = EventLabel;
        $scope.Label = Label;

        $scope.message = '';

        eventDetail.loadEvent = function () {

            promise = ModelUtils.get_request(Urls.get_event(eventDetail.event_id))
                .then(function (response) {
                    eventDetail.event = response;

                }, function (response) {
                    Toast.showToast(response.status + ' ' + response.statusText);
                });
        };

        eventDetail.loadEvent();

    });

})(window.angular);