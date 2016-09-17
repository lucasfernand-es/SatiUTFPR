(function () {
    'use strict';

    var app = angular.module('sati-factory', ['ngMaterial', 'ngMessages', 'material.svgAssetsCache']);


    /* -- Toast -- */
    var isDlgOpen;

    app.controller('ToastCtrl', function($scope, $mdToast, $mdDialog, $log, message) {
            $log.log("errors")

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

    app.factory('Label', function () {
        var Label = {
            tbd: function () {
                return 'A definir';
            },
            no_results: function () {
                return 'Nenhum resultado encontrado.';
            },
            clear_filter: function () {
                return 'Limpar Filtro';
            },
            none: function () {
                return 'Nenhum';
            },
            until: function () {
                return ' até ';
            },
            at: function () {
                return ' ás ';
            },
            open_sessions : function () {
                return 'Turmas Abertas';
            }
        };

        return Label;
    });


})(window.angular);