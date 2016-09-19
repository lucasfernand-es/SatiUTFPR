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

        $scope.sessions = [];


        $scope.errors = {};

        $scope.toggle = Addons.toggle;
        $scope.exists = Addons.exists;

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

        $scope.clear = function () {
            signupCtrl.has_account = false;
            $scope.isNewParticipant = true;
            $scope.showForm = true;
            $scope.search = {};
            signupCtrl.errors = [];
            signupCtrl.success = [];
            $scope.sessions = [];
            signupCtrl.signup_form.person = {};
            signupCtrl.signup_form.person.email = '';
            signupCtrl.signup_form.person.cpf = '';
            signupCtrl.signup_form.person.password = '';
            signupCtrl.signup_form.person.confirm_password = '';
            signupCtrl.signup_form.person.sessions = [];

        };

        signupCtrl.loadSessions = function () {

            promise = ModelUtils.get_request( Urls.get_all_sessions() );

            promise.then(function (response) { // Success
                var sessions = response.sessions;

                signupCtrl.sessions = sessions;

            }, function (response) {
                $log.log(response);
                Toast.showToast(response.status + ' ' + response.statusText);
            });

        };
        signupCtrl.loadSessions();

        signupCtrl.loadCategories = function () {

            signupCtrl.categories = [];
            var promise = ModelUtils.get_all(Urls.category());
            promise.then(function (response) { // Success
                angular.forEach(response.results, function (item) {
                    signupCtrl.categories.push(item);
                });
            }, function (result) { // Fail
                Toast.showToast(result.status + ' ' + result.statusText);
            });

        };
        signupCtrl.loadCategories();

        //noinspection JSAnnotator
        $scope.loadParticipantInfo = function () {

            signupCtrl.errors = [];
            signupCtrl.success = [];

            var send_user = {
                'email': signupCtrl.signup_form.person.email,
                'password': signupCtrl.signup_form.person.password
            };

            ModelUtils.post_request(Urls.get_sessions_user(), send_user, $scope.errors)
            .then(function (response) {
                $log.log('Xou da Xuxa');

                if(response.data.error) {
                    signupCtrl.errors.push({
                    'name': CRUDLabel.label_login(), 'message' : response.data.error_messages });
                    $scope.anchorTop();
                }
                else {
                    var sessions = response.data.sessions;
                    var person = response.data.person;
                    
                    angular.forEach(sessions, function (session) {
                        $scope.toggle(session.id, $scope.sessions);
                    });

                    signupCtrl.signup_form.person.id = person.id;
                    signupCtrl.signup_form.person.email = person.email;
                    signupCtrl.signup_form.person.cpf = person.cpf;
                    signupCtrl.signup_form.person.name = person.name;
                    signupCtrl.signup_form.person.academic_registry = parseInt(person.academic_registry, 10);
                    signupCtrl.signup_form.person.institution = person.institution;

                    signupCtrl.has_account = true;
                };


            }, function () {
                signupCtrl.errors = $scope.convertFields($scope.errors);
                $log.log('errors');
                $log.log(signupCtrl.errors);
                // the element you wish to scroll to.
            });


        };

        $scope.updateParticipation = function () {
            signupCtrl.errors = [];
            signupCtrl.success = [];


            signupCtrl.signup_form.person.sessions = $scope.sessions;

            ModelUtils.post_request(Urls.update_participant(), signupCtrl.signup_form.person, $scope.errors)
            .then(function (response) {

                var person = response.data.person;

                signupCtrl.success.push({
                    'name': CRUDLabel.label_person(), 'message' : person.name + ' - ' +
                    CRUDLabel.label_cpf() + ': '+ person.cpf + ' - ' +
                    CRUDLabel.label_email() + ': '+ person.email });

                var sessions = response.data.sessions;

                angular.forEach(sessions, function (session) {
                    var participation = {};
                    participation.name = CRUDLabel.label_participation();
                    var is_new = '';
                    if(!session.new)
                        is_new = ' - ' + Label.label_already_registered();
                    participation.message = session.event_name + is_new;

                    signupCtrl.success.push(participation);
                });
                $scope.showForm = false;

                $scope.anchorTop();

            }, function () {
                signupCtrl.errors = $scope.convertFields($scope.errors);
                $log.log('errors');
                $log.log(signupCtrl.errors);
                // the element you wish to scroll to.
            });
        };

        $scope.create = function () {

            signupCtrl.errors = [];
            signupCtrl.success = [];
            signupCtrl.signup_form.person.sessions = $scope.sessions;


            ModelUtils.post_request(Urls.add_new_participant(), signupCtrl.signup_form.person, $scope.errors)
            .then(function (response) {

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
                $scope.showForm = false;

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

        //href="#top"




    });


})(window.angular);