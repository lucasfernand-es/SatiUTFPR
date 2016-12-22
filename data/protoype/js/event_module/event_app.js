(function () {
    'use strict';

    var app = angular.module('Event', ['ngMaterial', 'ngMessages', 'material.svgAssetsCache',
                                            'eventDirectives' ]);

    app.controller('EventCtrl', EventCtrl);


    function EventCtrl($scope) {
        $scope.data = {
            selectedIndex: 0,
            secondLocked:  true,
            secondLabel:   "Item Two",
            bottom:        false
        };

        $scope.next = function() {
            $scope.data.selectedIndex = Math.min($scope.data.selectedIndex + 1, 2) ;
        };
        $scope.previous = function() {
            $scope.data.selectedIndex = Math.max($scope.data.selectedIndex - 1, 0);
        };
    }

})();