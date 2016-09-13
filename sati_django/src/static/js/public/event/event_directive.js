(function () {

    var app = angular.module('event-directive', []);

    app.directive('eventDetail', function() {
        return {
            restrict: 'E',
            transclude: true,
            templateUrl: '/static/templates/public/event/event_card.html',
        };
    });
/*
    app.directive("productDescriptions", function() {
        return {
          restrict: 'E',
          templateUrl: "../html/product-descriptions.html"
        };
    });
*/
})();
