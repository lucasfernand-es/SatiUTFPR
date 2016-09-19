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

        $scope.create = function () {
            signupCtrl.errors = {};

            signupCtrl.signup_form.person.name = 'nome';
            signupCtrl.signup_form.person.password = 'nome';
            signupCtrl.signup_form.person.confirm_password = 'nome';
            signupCtrl.signup_form.person.ra = 1371800;


            ModelUtils.post_request(Urls.add_new_participant(), signupCtrl.signup_form.person, $scope.errors)
            .then(function (response) {
                $log.log('de volta');
                $log.log(response);
            }, function () {
                $log.log($scope.convertErrorFields($scope.errors));
                signupCtrl.errors = $scope.convertErrorFields($scope.errors);
                $scope.anchorTop();
                // the element you wish to scroll to.
            });
        };

        $scope.anchorTop =function () {
            $location.hash('top');
            $anchorScroll();
        };

        $scope.test = function () {
            $log.log('lo');
        };

        $scope.convertErrorFields = Addons.convertErrorFields;

        $scope.clear = function () {
            $scope.search = {};
            signupCtrl.errors = {};
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