(function () {
    'use strict';

    var app = angular.module('Edition', ['ngMaterial', 'ngMessages']);

    app.controller('EditionCtrl', EditionCtrl);

    function EditionCtrl($scope) {

        var edition = this;

        edition.name = "SATI 2016";
        edition.theme = "Acessibilidade";

        edition.initial_date = new Date(Date.now());
        edition.final_date = new Date(Date.now() + 1);
        edition.status = true;

    }


    angular.module('inputErrorsApp', ['ngMaterial', 'ngMessages'])
    .controller('AppCtrl', function($scope) {
      $scope.project = {
        description: 'Nuclear Missile Defense System',
        rate: 500
      };
    });

    angular
  .module('inputIconDemo', ['ngMaterial', 'ngMessages'])
  .controller('DemoCtrl', function($scope) {
    $scope.user = {
      name: 'John Doe',
      email: '',
      phone: '',
      address: 'Mountain View, CA',
      donation: 19.99
    };
  });

})();