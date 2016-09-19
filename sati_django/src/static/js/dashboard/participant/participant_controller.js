(function () {
    'use strict';

    var app = angular.module('participant-controller',
        ['public-directive', 'ngMaterial', 'ngMessages']);



    app.controller('ParticipantCtrl', function EventDetailCtrl($scope, $log, $http, $mdDialog,
                                                               ModelUtils, Urls, Toast, Label, Addons,
                                                               EventLabel, CRUDLabel) {
        var participantCtrl = this;
        participantCtrl.events = [];
        participantCtrl.modifiedParticipations = [];
        var promise;

        $scope.Label = Label;
        $scope.CRUDLabel = CRUDLabel;


        participantCtrl.loadParticipants = function () {
            promise = ModelUtils.get_request(Urls.get_all_participants())
                .then(function (response) {
                    $log.log(response.events);

                    participantCtrl.events = response.events;

                }, function (response) {
                    Toast.showToast(response.status + ' ' + response.statusText);
                });
        };

        $scope.log = function () {
          $log.log('init');
        };

        participantCtrl.loadParticipants();

        participantCtrl.addModifiedParticipant = function (participation, event) {

            participation.event = event;

            if( !Addons.exists(participation, participantCtrl.modifiedParticipations) ) {
                participantCtrl.modifiedParticipations.push(participation);
            };

            var message = participation.is_confirmed?
                Label.label_participant_is_confimed_true_lower() :
                Label.label_participant_is_confimed_false_lower();

            Toast.showToast('Participação de '
                + participation.name
                + ' alterada em '
                + participation.event.name
                + ' para '
                + message + '.');

            $log.log(participantCtrl.modifiedParticipations);
        };

        participantCtrl.saveParticipations = function () {
            $mdDialog.cancel();
            $log.log('oi');

            participantCtrl.loadParticipants();
        };

        participantCtrl.confirmParticipations = function(ev) {
            $mdDialog.show({
                controller: ConfirmParticipationsCtrl,
                locals: {
                    participations : participantCtrl.modifiedParticipations,
                    saveParticipations : participantCtrl.saveParticipations
                },
                templateUrl: '/static/templates/dashboard/participation/confirm_participation_list.html',
                parent: angular.element(document.body),
                targetEvent: ev,
                clickOutsideToClose: true,
                fullscreen: $scope.customFullscreen // Only for -xs, -sm breakpoints.
            })
        };


        function ConfirmParticipationsCtrl($scope, $mdDialog, participations, saveParticipations, Label) {
            $scope.participations = participations;
            $scope.saveParticipations = saveParticipations;
            $scope.Label = Label;
            $log.log('olha elaaaaaa');

            $scope.removeParticipation = function (participation) {
                var index = $scope.participations.indexOf(participation);
                $scope.participations.splice(index, 1);
            };


            $scope.hide = function () {
                $mdDialog.hide();
            };

            $scope.cancel = function () {
                $mdDialog.cancel();
            };
        }

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
