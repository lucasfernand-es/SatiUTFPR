(function () {
    'use strict';

    var app = angular.module('participant-controller',
        ['ngRoute', 'public-directive', 'ngMaterial', 'ngMessages']);



    app.controller('ParticipantCtrl', function EventDetailCtrl($scope, $log, $http,
                                                               ModelUtils, Urls, Toast, Label,
                                                               EventLabel) {
        var participantCtrl = this;

        var promise;


        participantCtrl.loadParticipants = function () {

        };

    });


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
