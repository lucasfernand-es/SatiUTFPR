(function () {
    'use strict';

    var app = angular.module('event-factory', []);

    app.factory('Label', function () {
        var Label = {
            tbd: function () {
                return 'A definir';
            },
            filter_label_event_name : function () {
                return 'Nome do Evento';
            },
            filter_label_filter_event : function () {
                return 'Encontre Eventos';
            },
            filter_label_event_begin_date : function () {
                return 'Eventos até';
            }
        };

        return Label;
    });

})(window.angular);