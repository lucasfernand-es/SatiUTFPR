(function () {
    'use strict';

    var app = angular.module('crud-urls-factory', []);

    app.factory('Urls', function () {
        var Urls = {
            event: function () {
                return '/api/event/';
            },
            session: function () {
                return '/api/session/';
            },
            edition: function () {
                return '/api/edition/';
            },
            room: function () {
                return '/api/room/';
            },
            person: function () {
                return '/api/person/';
            },
        };

        return Urls;
    });

})(window.angular);