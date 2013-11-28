angular.module('project', ['restangular']).
  config(function($routeProvider, RestangularProvider) {
    $routeProvider.
      when('/', {
        controller:ListCtrl, 
        templateUrl:'list.html'
      }).
      when('/editar/evento/:eventoID', {
        controller:EditCtrl, 
        templateUrl:'detail.html',
        resolve: {
          evento: function(Restangular, $route){
            return Restangular.one('evento', $route.current.params.eventoID).get();
          }
        }
      }).
      when('/new', {controller:CreateCtrl, templateUrl:'detail.html'}).
      otherwise({redirectTo:'/'});
      
      RestangularProvider.setBaseUrl('http://intercambios-node.herokuapp.com/');
      
      RestangularProvider.setRequestInterceptor(function(elem, operation, what) {
        
        if (operation === 'put') {
          elem.id = undefined;
          return elem;
        }
        return elem;
      })
  });


function ListCtrl($scope, Restangular) {
   Restangular.all("eventos/usuario/"+usuario_actual).getList().then(function(projects) {
     $scope.projects = projects;
   });
}


function CreateCtrl($scope, $location, Restangular) {
  $scope.save = function() {
    Restangular.all('evento').post($scope.evento).then(function(project) {
      $location.path('/list');
    });
  }
}

function EditCtrl($scope, $location, Restangular, evento) {
  var original = evento;
  $scope.evento = Restangular.copy(original);
  
  

  $scope.isClean = function() {
    return angular.equals(original, $scope.evento);
  }

  $scope.destroy = function() {
    original.remove().then(function() {
      $location.path('/list');
    });
  };

  $scope.save = function() {
    $scope.evento.put().then(function() {
      $location.path('/list');
    });
  };
}