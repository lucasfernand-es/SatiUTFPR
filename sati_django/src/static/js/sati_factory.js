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

    app.factory('Addons', function ($log, ErrorLabel) {
        var Addon = {
            toggle : function (item, list) {
                var idx = list.indexOf(item);
                if (idx > -1) {
                    list.splice(idx, 1);
                }
                else {
                    list.push(item);
                }
            },
            exists : function (item, list) {
                    return list.indexOf(item) > -1;
            },
            convertErrorFields : function (errors) {
                $log.log(errors);
                var newErrors = [];

                angular.forEach(errors, function (error, key) {
                    var new_error = {};
                    new_error.name = ErrorLabel(key);
                    new_error.message = error;

                    newErrors.push(new_error);
                });



                return newErrors;
            },


        };
        return Addon;
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
            by: function () {
                return ' por ';
            },
            open_sessions : function () {
                return 'Turmas Abertas';
            },
            no_spot : function () {
                return 'Esgotado';
            },
            occurence: function () {
                return 'Cronograma';
            }
        };

        return Label;
    });


})(window.angular);