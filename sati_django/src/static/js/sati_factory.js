(function () {
    'use strict';

    var app = angular.module('sati-factory', ['ngMaterial', 'ngMessages', 'material.svgAssetsCache']);


    /* -- Toast -- */
    var isDlgOpen;

    app.controller('ToastCtrl', function($scope, $mdToast, $mdDialog, $log, message) {

        $scope.text = message;

        $scope.closeToast = function() {
            if (isDlgOpen) return;

            $mdToast.hide().then(function() {
                isDlgOpen = false;
            });
      };
    });

    app.factory('Toast', function ($mdToast) {

        var Toast = {
            showToast : function(text) {
                $mdToast.show({
                    hideDelay   : 5000,
                    position    : 'top left right',
                    locals: {message: text},
                    controller  : 'ToastCtrl',
                    controllerAs : 'toastCtrl',
                    templateUrl : '/static/templates/sati/toast.html'
                });
            }
        };

        return Toast;

    });


})(window.angular);