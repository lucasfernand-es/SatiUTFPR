(function () {

    var app = angular.module('sati-directive', []);

    app.directive('warnMessage', function() {
        return {
            restrict: 'E',
            templateUrl: '/static/templates/sati/warn-message.html',
            controller: function ($scope, $log) {
            },
        };
    });

})();
