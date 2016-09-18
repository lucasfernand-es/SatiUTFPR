(function () {
    'use strict';

    var app = angular.module('signup-controller',
        ['signup-factory', 'signup-directive', 'public-directive', 'ngMaterial', 'ngMessages']);


    //var ListDropdown = angular.module('ListDropdown', []);


    app.controller('SignupCtrl', function($scope, $log, $http,
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

        $scope.Instituions = ['UTFPR', 'UEPG'];
        $scope.UTFPR = 'UTFPR';

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

            ModelUtils.post_request(Urls.add_new_participant(), signupCtrl.signup_form.person, $scope.errors)
                .then(function () {
                    $log.log($scope);
                });
        };

        $scope.clear = function () {
            signupCtrl.signup_form.person = {};
            signupCtrl.signup_form.person.sessions = [];
        };

        signupCtrl.loadSessions();

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