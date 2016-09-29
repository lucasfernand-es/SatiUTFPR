(function () {
    'use strict';

    var app = angular.module('participant-controller',
        ['public-directive', 'participant-filter', 'ngMaterial', 'ngMessages']);



    app.controller('ParticipantCtrl', function EventDetailCtrl($scope, $log, $http, $mdDialog,
                                                               ModelUtils, Urls, Toast, Label, Addons,
                                                               EventLabel, CRUDLabel) {
        var participantCtrl = this;
        participantCtrl.events = [];
        participantCtrl.modifiedParticipants = [];
        var promise;

        $scope.Label = Label;
        $scope.CRUDLabel = CRUDLabel;

        participantCtrl.clear = function () {
            participantCtrl.modifiedParticipants = [];
            participantCtrl.loadParticipants();
        };


        participantCtrl.loadParticipants = function () {
            promise = ModelUtils.get_request(Urls.get_all_participants())
                .then(function (response) {

                    angular.forEach(response.events, function (event) {
                        angular.forEach(event.sessions, function (session) {
                            session.filterParticipant = session.participants;
                        });
                    });

                    participantCtrl.events = response.events;
                    participantCtrl.hasEvents = response.events.length > 0;

                }, function (response) {
                    Toast.showToast(response.status + ' ' + response.statusText);
                });
        };

        participantCtrl.loadParticipants();

        participantCtrl.addModifiedParticipant = function (participant) {

            if( !Addons.exists(participant, participantCtrl.modifiedParticipants) ) {
                participantCtrl.modifiedParticipants.push(participant);
            };

            var message = participant.is_confirmed?
                Label.label_participant_is_confimed_true_lower() :
                Label.label_participant_is_confimed_false_lower();

            Toast.showToast('Participação de '
                + participant.name
                + ' alterada em '
                + participant.event_name
                + ' para '
                + message + '.');
        };


        participantCtrl.saveParticipants = function () {
            $mdDialog.cancel();

            participantCtrl.errors = [];
            participantCtrl.success = [];

            var send_request = {'participants': participantCtrl.modifiedParticipants};


            promise = ModelUtils.post_request(Urls.confirm_participant(), send_request, $scope.errors)
            .then(function (response) {

                if ( response.data.empty )
                {
                    participantCtrl.errors.push({
                            'name': 'Lista Vazia',
                            'message': response.data.error_messages
                        });
                }
                else {
                    angular.forEach(response.data.success_message, function (success) {

                        if (!success.participant.is_new) {
                            var message = success.participant.is_confirmed?
                                'confirmado(a)' :
                                'não confirmado(a)';

                            participantCtrl.success.push({
                                'name': 'Participante',
                                'message': success.participant.name + ' ' + message + ' para ' + success.participant.event_name
                            });
                        };
                    });

                    angular.forEach(response.data.error_messages, function (error) {
                        participantCtrl.errors.push({
                            'name': error.error_type,
                            'message': 'Não foi possível modificar o estado de ' +
                            error.participant.name + ' em ' + error.participant.event_name
                        });
                    });

                    participantCtrl.Response(null, participantCtrl.success, participantCtrl.errors);
                };


                participantCtrl.clear();
            }, function (response) {
                participantCtrl.errors = $scope.convertFields($scope.errors);
                participantCtrl.Response(null, [], participantCtrl.errors);
                $log.log('errors');
                $log.log($scope.errors);
                Toast.showToast(response.status + ' ' + response.statusText);
            });


        };

        participantCtrl.Response = function(ev, success, errors) {
            $mdDialog.show({
                controller: ResponseCtrl,
                locals: {
                    success : success,
                    errors : errors,
                    title: 'Atualização'
                },
                templateUrl: '/static/templates/dashboard/response.html',
                parent: angular.element(document.body),
                targetEvent: ev,
                clickOutsideToClose: true,
                fullscreen: $scope.customFullscreen // Only for -xs, -sm breakpoints.
            })
        };

        function ResponseCtrl($scope, $mdDialog, Label, success, errors, title) {
            $scope.title = title;
            $scope.success = success;
            $scope.errors = errors;
            $scope.Label = Label;

            $scope.hide = function () {
                $mdDialog.hide();
            };

            $scope.cancel = function () {
                $mdDialog.cancel();
            };
        };

        participantCtrl.confirmParticipants = function(ev) {
            $mdDialog.show({
                controller: ConfirmParticipantsCtrl,
                locals: {
                    addModifiedParticipant : participantCtrl.addModifiedParticipant,
                    participants : participantCtrl.modifiedParticipants,
                    saveParticipants : participantCtrl.saveParticipants
                },
                templateUrl: '/static/templates/dashboard/participation/confirm_participation_list.html',
                parent: angular.element(document.body),
                targetEvent: ev,
                clickOutsideToClose: true,
                fullscreen: $scope.customFullscreen // Only for -xs, -sm breakpoints.
            })
        };


        function ConfirmParticipantsCtrl($scope, $mdDialog, participants, saveParticipants, addModifiedParticipant, Label) {
            $scope.participants = participants;
            $scope.saveParticipants = saveParticipants;
            $scope.Label = Label;
            $scope.addModifiedParticipant = addModifiedParticipant;

            $scope.removeParticipation = function (participation) {
                var index = $scope.participants.indexOf(participation);
                $scope.participants.splice(index, 1);
            };


            $scope.hide = function () {
                $mdDialog.hide();
            };

            $scope.cancel = function () {
                $mdDialog.cancel();
            };
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
