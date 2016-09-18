(function () {
    'use strict';

    var app = angular.module('signup-controller',
        ['signup-factory', 'signup-directive', 'public-directive', 'ngMaterial', 'ngMessages']);


    //var ListDropdown = angular.module('ListDropdown', []);


    app.controller('SignupCtrl', function($scope, $log, $http, $window, $location, $anchorScroll,
                                          SignupLabel, Label, CRUDLabel, ErrorLabel,
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

        $scope.convertErrorFields = Addons.convertErrorFields;

        $scope.clear = function () {
            $scope.anchorTop();
            signupCtrl.errors = {};
            signupCtrl.signup_form.person = {};
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