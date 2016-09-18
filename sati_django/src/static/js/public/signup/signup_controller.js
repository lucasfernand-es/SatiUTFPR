(function () {
    'use strict';

    var app = angular.module('signup-controller',
        ['signup-factory', 'signup-directive', 'public-directive', 'ngMaterial', 'ngMessages']);


    app.controller('SignupCtrl', function($scope, $log,
                                          SignupLabel, Label, CRUDLabel,
                                          ModelUtils, Urls,
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

        signupCtrl.signup_form.person = {};
        signupCtrl.signup_form.person.sessions = [];

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

        signupCtrl.loadSessions();

        $scope.Instituions = ['UTFPR', 'UEPG'];
        $scope.UTFPR = 'UTFPR';


        signupCtrl.create = function () {
            var person = {}


            person.name = 'Lucas';

            person.email = 'email@email.com';
            person.password = '123';
            person.instituion = 'UTFPR';
            person.cpf = '37789417800';
            person.academic_registry = '1371800';
            person.role = 1;
            person.is_active = true;

            $log.log(person);

            $log.log('passou');

            $log.log($scope.errors);

            ModelUtils.create(Urls.test_person(), person, $scope.errors)
                .then(function () {
                    $log.log($scope.errors);
                });

            /*ModelUtils.create(Urls.add_new_participant(), signupCtrl.signup_form.person, $scope.errors)
                .then(function () {
                    $log.log($scope.errors);
                });*/



            $log.log($scope);
        };

        $scope.toggle = function (item, list) {
            var idx = list.indexOf(item);
            if (idx > -1) {
            list.splice(idx, 1);
            }
            else {
            list.push(item);
            }
        };

        $scope.exists = function (item, list) {
            return list.indexOf(item) > -1;
        };




    });


})(window.angular);