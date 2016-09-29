(function () {
    var app = angular.module('eventDirectives', []);

    var d = angular.module()
    app.directive('event', function() {
      return {
        restrict: 'E',
        /*
          E = Element
          A = Attribute
        */
        templateUrl: '../html/event.html'
      };
    });

    app.directive('eventSession', function() {
      return {
        restrict: 'E',
        templateUrl: '../html/event_session.html'
      };
    });

    app.directive('eventOccurrence', function() {
      return {
        restrict: 'E',
        templateUrl: '../html/event_occurrence.html'
      };
    });

})();
