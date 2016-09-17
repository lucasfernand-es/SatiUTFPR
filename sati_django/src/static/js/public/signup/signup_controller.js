(function () {
    'use strict';

    var app = angular.module('signup-controller',
        ['signup-factory', 'signup-directive', 'ngMaterial', 'ngMessages']);


    app.controller('SignupCtrl', function($scope, $log,
                                          SignupLabel, Label, CRUDLabel,
                                          ModelUtils, Urls,
                                          FieldSize) {
        var signupCtrl = this;
        var promise = '';
        signupCtrl.signup_form = {};

        $scope.Label = Label;
        $scope.SignupLabel = SignupLabel;
        $scope.CRUDLabel = CRUDLabel;
        $scope.FieldSize = FieldSize;
        $scope.max_length_error = '';

        signupCtrl.signup_form.person = {};

        signupCtrl.loadEvents = function () {


        };

        signupCtrl.loadEvents();


        signupCtrl.create = function () {
          $log.log(signupCtrl.signup_form.person);
        };



    });


})(window.angular);