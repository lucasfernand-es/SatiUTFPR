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