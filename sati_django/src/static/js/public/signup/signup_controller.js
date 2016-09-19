(function () {
    'use strict';

    var app = angular.module('signup-controller',
        ['signup-factory', 'signup-directive', 'ngRoute', 'public-directive', 'ngMaterial', 'ngMessages']);



    app.controller('LoginCtrl', function ($scope, $log, $location, $window,
                                          Label, CRUDLabel,
                                          ModelUtils, Urls, Addons) {

        var loginCtrl = this
        $scope.Label = Label;
        $scope.CRUDLabel = CRUDLabel;


        loginCtrl.login_form = {};
        $scope.convertErrorFields = Addons.convertErrorFields;

        $scope.login = function () {
            $log.log(loginCtrl.login_form);

            //$window.location.href = '/index.html';
            ModelUtils.post_request(Urls.login(), loginCtrl.login_form, $scope.errors)
            .then(function () {
            }, function () {
                $log.log($scope.convertErrorFields($scope.errors));
                loginCtrl.errors = $scope.convertErrorFields($scope.errors);
            });

        };

    });

    app.controller('SignupCtrl', function($scope, $log, $http, $window, $location, $anchorScroll,
                                          SignupLabel, Label, CRUDLabel,
                                          ModelUtils, Urls, Addons,
                                          FieldSize, Toast) {
        var signupCtrl = this;
        var promise;
        signupCtrl.signup_form = {};
        $scope.Label = Label;
        $scope.SignupLabel = SignupLabel;
        $scope.CRUDLabel = CRUDLabel;
        $scope.FieldSize = FieldSize;
        $scope.max_length_error = '';

        $scope.message = Label.no_results();

        $scope.Institutions = ['UTFPR', 'UEPG'];
        $scope.UTFPR = 'UTFPR';

        $scope.isNewParticipant = true;


        signupCtrl.loadSessions = function () {

            promise = ModelUtils.get_request( Urls.get_all_sessions() );

            promise.then(function (response) { // Success
                $log.log(response);
                var sessions = response.sessions;

                signupCtrl.sessions = sessions;

            }, function (response) {
                $log.log(response);
                Toast.showToast(response.status + ' ' + response.statusText);
            });

        };

        //noinspection JSAnnotator
        $scope.loadParticipantInfo = function () {



        };

        $scope.create = function () {

            signupCtrl.errors = [];
            signupCtrl.success = [];

            signupCtrl.signup_form.person.name = 'Lucas Emanuel Nome Grande';
            signupCtrl.signup_form.person.password = 'nome';
            signupCtrl.signup_form.person.confirm_password = 'nome';
            signupCtrl.signup_form.person.ra = 1371800;


            ModelUtils.post_request(Urls.add_new_participant(), signupCtrl.signup_form.person, $scope.errors)
            .then(function (response) {
                $log.log(response.data);

                var person = response.data.person;

                signupCtrl.success.push({
                    'name': CRUDLabel.label_person(), 'message' : person.name + ' - ' +
                    CRUDLabel.label_cpf() + ': '+ person.cpf + ' - ' +
                    CRUDLabel.label_email() + ': '+ person.email });

                var sessions = response.data.sessions;

                angular.forEach(sessions, function (session) {
                    var participation = {};
                    participation.name = CRUDLabel.label_participation();
                    participation.message = session.event_name;

                    signupCtrl.success.push(participation);
                });

                $log.log(signupCtrl.success);

                $scope.anchorTop();

            }, function () {
                signupCtrl.errors = $scope.convertFields($scope.errors);
                $log.log('errors');
                $log.log(signupCtrl.errors);
                $scope.anchorTop();
                // the element you wish to scroll to.
            });
        };

        $scope.anchorTop =function () {
            $location.hash('top');
            $anchorScroll();
        };

        $scope.convertFields = Addons.convertFields;

        $scope.clear = function () {
            $scope.search = {};
            signupCtrl.errors = [];
            signupCtrl.success = [];
            signupCtrl.signup_form.person = {};
            signupCtrl.signup_form.person.email = '';
            signupCtrl.signup_form.person.cpf = '';
            signupCtrl.signup_form.person.password = '';
            signupCtrl.signup_form.person.confirm_password = '';
            signupCtrl.signup_form.person.sessions = [];
        };

        signupCtrl.loadSessions();
        $scope.clear();

        $scope.errors = {};

        $scope.toggle = Addons.toggle;

        $scope.exists = Addons.exists;

        //href="#top"




    });


})(window.angular);