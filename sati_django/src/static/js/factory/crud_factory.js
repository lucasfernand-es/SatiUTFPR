(function () {
    'use strict';

    var app = angular.module('crud-factory', [ 'crud-urls-factory'
                                        ]);

    app.factory('ModelUtils', function($http, $log) {


        var handleErrors =  function(serverResponse, status, errorDestination) {
            if (angular.isDefined(errorDestination)) {
                if (status >= 500) {
                    errorDestination.form = 'Server Error: ' + status;
                } else if (status >= 401) {
                    errorDestination.form = 'Unauthorized Error: ' + status;
                } else {
                    angular.forEach(serverResponse, function(value, key) {
                        if (key != '__all__') {
                            errorDestination[key] = angular.isArray(value) ? value.join("<br/>") : value;
                        } else {
                            errorDestination.form = errorDestination.form || '' + key + ':' + angular.isArray(value) ? value.join("<br/>") : value;
                        }
                    });
                }
            }
        };


        var ModelUtils = {
            get: function(url, id) {
                return $http.get(url + id + '/').then(function(response){
                        //$log.log('get');
                        //$log.log(response.data);
                        return response.data;
                    }
                );
            },

            get_all: function(url) {
                return $http.get(url).then(function(response){
                        //$log.log('get');
                        //$log.log(response.data);
                        return response.data;
                    }
                );
            },

            create: function(url, obj, errors) {
                $log.log(obj);
                obj.important = true;

                return $http.post(url, obj).
                    success(function(response, status, headers, config) {
                        angular.extend(obj, response);
                    }).
                    error(function(response, status, headers, config) {
                        handleErrors(response, status, errors);
                    });
            },

            save: function(url, obj, errors) {
                $log.log(obj);
                if (angular.isDefined(obj.id)) {
                    return $http.put(url + obj.id + '/', obj).
                            success(function(response, status, headers, config) {
                                angular.extend(obj, response);
                            }).
                            error(function(response, status, headers, config) {
                                $log.log(errors);
                                handleErrors(response, status, errors);
                            });
                } else {
                    return this.create(url, obj, errors);
                }
            },

            del: function(url, obj) {
                return $http.delete(url + obj.id + '/');
            }
        };

        return ModelUtils;

    });


    /*
    app.factory('EventFactory', function ($log, ModelUtils, Urls, EditionFactory) {

        var get_edition = function (id) {
            return EditionFactory.get(id);
        };

        var EventFactory = {
            get: function(id) {
                return ModelUtils.get(Urls.event(), id);
            },
            get_all: function() {
                return ModelUtils.get_all(Urls.event());
            }
        };

        return EventFactory;
    });
    */

})(window.angular);
