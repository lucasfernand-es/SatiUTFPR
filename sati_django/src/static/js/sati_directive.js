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

})();