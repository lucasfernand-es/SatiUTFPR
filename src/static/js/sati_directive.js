(function () {

    var app = angular.module('sati-directive', []);

    app.directive('warnMessage', function() {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/sati/message.html',
            controller: function ($scope, $log) {
                $scope.style = 'mdl-color--red-A700';
            },
            controllerAs: 'warnMessageCtrl',
        };
    });

    app.directive('noresultMessage', function() {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/sati/message.html',
            controller: function ($scope, $log) {
                $scope.style = 'mdl-color--light-blue-700';
            },
            controllerAs: 'MessageCtrl',
        };
    });

    app.directive('errorResponse', function() {
        return {
            restrict: 'E',
            scope : {
                messages : '='
            },
            transclude: true,
            templateUrl: '/static/templates/sati/crud_response.html',
            controller: function ($scope, $log, CRUDLabel) {
                var responseCtrl = this;
                //responseCtrl.messages = $scope.messages;

                responseCtrl.style = 'error';
                responseCtrl.text_style = 'mdl-color-text--red-600';
                responseCtrl.title_icon = 'report_problem';
                responseCtrl.item_icon =  'priority_high';
                responseCtrl.title = CRUDLabel.label_insert_error();

            },
            controllerAs: 'responseCtrl',
        };
    });

    app.directive('successResponse', function() {
        return {
            restrict: 'E',
            scope : {
                messages : '='
            },
            transclude: true,
            templateUrl: '/static/templates/sati/crud_response.html',
            controller: function ($scope, $log, CRUDLabel) {
                var responseCtrl = this;

                responseCtrl.style = 'success';
                responseCtrl.text_style = 'mdl-color-text--green-500';
                responseCtrl.title_icon = 'done_all';
                responseCtrl.item_icon =  'add_box';
                responseCtrl.title = CRUDLabel.label_insert_success();

            },
            controllerAs: 'responseCtrl',
        };
    });

    var compareTo = function() {
        return {
            require: "ngModel",
            scope: {
                otherModelValue: "=compareTo"
            },
            link: function(scope, element, attributes, ngModel) {

                ngModel.$validators.compareTo = function(modelValue) {
                    return modelValue == scope.otherModelValue;
                };

                scope.$watch("otherModelValue", function() {
                    ngModel.$validate();
                });
            }
        };
    };
    app.directive("compareTo", compareTo);
/*
    var backendError = function() {
        return {
            require: "ngModel",
            scope: {
                relatedError: "=backendError"
            },
            link: function(scope, element, attributes, ngModel) {

                ngModel.$validators.backendError = function(value) {
                    console.log(value);
                    console.log('entrou');
                    return false;
                };

                scope.$watch("relatedError", function() {
                    console.log('hmmm');
                    ngModel.$validate();
                });
            }
        };
    };
    app.directive("backendError", backendError);
*/
})();