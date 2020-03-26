
var cityArray = [];
var zipcodeArray = [];

var city = function(name, code) {
  this.name = name;
  this.code = code;
  cityArray.push(this);
  zipcodeArray.push(this.code);
}

var Chartres = new city("Chartres", '28000');
Chartres.candidat = "Jean Pierre GEORGES";
Chartres.message = "Toujours là";

var Montreuil = new city("Montreuil", '93100');
Montreuil.candidat = "Patrick BESSAC";
Montreuil.message = "Génial, un 5eme marché bio va ouvrir";

var Issy = new city('Issy-les-Moulineaux', '92130');
Issy.candidat = 'Andre SANTINI';
Issy.message = 'Le plus vieil habitant et probable fondateur de la ville des Hauts de Seine a remporté haut la main grâce à la coalition traditionnelle corses + arméniens + vieux';

var Levallois = new city('Levallois-Perret', '92300');
Levallois.candidat = 'PATRICK ET ISABELLE!!';
Levallois.message = 'Nan je déconne.';

var Boulogne = new city('BoulBi', '92100');
Boulogne.candidat = 'Le Duc de Boulogne';
Boulogne.message = "L'officiel, Pierre Christophe Baguet, élu avec 56%. Il a souvent était trahi, en vrai rien de nouveau. Ce sera votre Cavaliero";

var Corbeil = new city('Corbeil-Essonnes', '91100');
Corbeil.candidat = 'Deuxième tour, Onizuka';
Corbeil.message = "J'ai vu yencli voter blanc dans l'escalier. C'est en ballotage. ça va se compter au DD le deuxieme tour.";

var Okabe = new city('Le KB', '94270');
Okabe.candidat = 'Deuxième tour';
Okabe.message = "Comme d'hab, ça a voté au PMU. Pas vrai JM Nicolle?";

var Angers = new city('Angers', '49000');
Angers.candidat = 'Christophe Béchu';
Angers.message = "Fifou je savais que t'allais checker. C'est bon, ton Boy est toujours là";

var Beziers = new city('Béziers', '34500');
Beziers.candidat = "Robert Ménard";
Beziers.message = "Comme quoi une caméra dans le c** de chaque habitant ça marche";

var Troyes = new city("Troyes", '10000');
Troyes.candidat = "L'ex-Harry Potter du Gouvernement";
Troyes.message = "Le Maire des Maires a mis sa mère à l'opposition";

var Tourcoing = new city('Tourcoing', '59200');
Tourcoing.candidat = 'Gerard DARMANIN';
Tourcoing.message = 'Le ministre des Comptes publics est bien là.';

var Lille = new city('Lille', '59000');
Lille.candidat = 'Deuxième tour';
Lille.message = "Non. Elle n'est pas passée. Pas encore.";

var Marseille = new city('Marseille-sa-mère', '13000');
Marseille.candidat = 'Robert TERO';
Marseille.message = "En vrai ch'ais pas. J'ai pas regardé la série.";

var Maintenon = new city('Maintenon', '28130');
Maintenon.candidat = 'Thomas LAFORGE';
Maintenon.message = "Salut Julien . T'as vu j'y ai pensé";

var Nogent = new city('Nogent-le-Rotrou', '28130');
Nogent.candidat = 'Deuxième tour';
Nogent.message = "Il y aura une Triangulaire. Et pour votre info, en japonais, ménage à trois ça se dit SANKAKU KANKEI: une relation triangulaire. Voilà, si vous regardez Terrace House sur Netflix vous l'avez probablement entendu.";

var Reims = new city('Reims', '51100');
Reims.candidat = 'Arnaud ROBINET';
Reims.message = "Le candidat LR a gagné au premier tour 66% des suffrages. Voilà voilà.";

var Frejus = new city('Fréjus', '83600');
Frejus.candidat = 'LES MECHANTS';
Frejus.message = '';

var Meaux = new city('Meaux', '77100');
Meaux.candidat = 'Jean François COPE';
Meaux.message = "Bravo, bien joué, t'as gagné un petit pain au chocolat ";

var Barcelone = new city('Barcelona', '08001');
Barcelone.candidat = 'Manuel VALLS';
Barcelone.message = "Casi Manu, t'étais pas loin. Enfin si quand même.";

var Bruxelles = new city('Bruxelles', '1000');
Bruxelles.candidat = 'Bourgmestre Costre';
Bruxelles.message = "Merci d'avoir pensé à nos amis belges.";

var Milano = new city('Milano', '20124');
Milano.candidat = 'NATHALIE';
Milano.message = "Courage championne, la bise à Karl";

var Madrid = new city('Madrid', '28001');
Madrid.candidat = 'El niño Almeida';
Madrid.message = "TIERNO GALVAN: EL MEJOR ALCADE DE MADRID;DESDE MADRID HASTA EL CIELO.";

var Charleroi = new city('Charleroi', '6000');
Charleroi.candidat = 'Paul MAGNETTE';
Charleroi.message = "L'ancien grand pourfandeur des accords UE-Canada va très bien. Il est maintenant Bourgmestre de Charleroi. La dernière ville où des grandes entreprises tiendraient un tribunal arbitral international (de toutes façons il manque un hôtel 5 étoiles).";

var Paris = new city('Paris', '75000');
Paris.candidat = 'BENJI GRIVEAUX HAHAHHA';
Paris.message = "Nan en vrai il faut attendre non pas un mais deux tours pour connaître le résultat. Mme Hidalgo est en tête; Mme Buzin a jeté l'éponge; Mme Dati est réélue dans le 7eme.";

var Paris_sept = new city('Paris VIIe', '75007');
Paris_sept.candidat = 'Rachida Dati';
Paris_sept.message = "D'après Paris Match elle a fait une bonne campagne de terrain.";

var Paris_onze = new city('Paris XIe', '75011');
Paris_onze.candidat = 'Deuxieme tour';
Paris_onze.message = "Anne Hidalgo se présentait dans cet arrondissement. Saviez-vous qu'elle était née à Cadix? Una Gaditana! ça vaut bien une chanson de flamenco-rock: https://www.youtube.com/watch?v=U4il05Pt5Nk";

var Paris_quatorze = new city('Paris XIVe', '75014');
Paris_quatorze.candidat = 'Deuxieme tour';
Paris_quatorze.message = "Cedric Villani, qui se présentait dans cet arrodissement, n'obtient que 12%. Vous saviez que parmi les problèmes mathématiques sur lesquels il travaillait il y avait le problème de l'optimisation des transports de Monge? ça a l'air bien plus intéressant que la théorie pour laquelle il a reçu la médaille Fields, j'ai lu son livre, j'ai rien pigé.";

var Montcuq = new city('Montcuq', '46800');
Montcuq.candidat = 'Daniel Prevost';
Montcuq.message = "C'était très serré";

var Nice = new city("Nice", '84000');
Nice.candidat = "";
Nice.message = "Si vous êtes là c'est probablement pour avoir des nouvelles de Monsieur Estrosi, infecté par le Covid-19, voici son twitter: twitter.com/cestrosi Pour les élections, il n'est pas passé loin de la réélection (47%)";

var Henin = new city('Hénin-Beaumont', '62110');
Henin.candidat = 'Steeve';
Henin.message = 'He beh. Ils sont solides là bas';

var Coulommiers = new city('Coulommiers comme le fromage', '77120');
Coulommiers.candidat = 'Franck Riester';
Coulommiers.message = 'Le Ministre de la Culture était le premier membre du Gouvernement contaminé. Vous pouvez prendre de ses nouvelles ici: twitter.com/franckriester (en vrai ça sert à rien, il ne parle pas de lui, il ne fait que retweeter ton boss)';

var Bobigny = new city('Bobigny', '93000');
Bobigny.candidat = 'KYLIAN!!!';
Bobigny.message = "Wait, 93000? C'est la préfécture? J'étais certain que c'était Saint-Denis, c'est dans le nom du département?!! Pour avoir des nouvelles de Kylian, allez sur le site de l'Equipe, les mecs n'ont plus rien sur quoi écrire, ils lui font eux-même la température maintenant.";

var Lyon = new city('ONLY LYON', '69000');
Lyon.candidat = 'Deuxième tour';
Lyon.message = "Le candidat des verts, Grégory Doucet est en tête. D'ailleurs, elle devient quoi Najat Vallaud-Belkacem?";

var Vichy = new city('Vichy', '03200');
Vichy.candidat = 'Deuxième tour';
Vichy.message = "Salut Lavaud";

var Bordeaux = new city('Bordeaux', '33000');
Bordeaux.candidat = 'Deuxième tour';
Bordeaux.message = "La vache, depuis 1947, tous les candidats gaullistes ont été élus au premier tour. Nicolas Florian il doit avoir les boules. Il est talloné par les écolos.";


function search_zip_code() {
  $("#city_name").text("Connais pas");
  //var codeInput = parseInt($("#zipcode").val());
  var codeInput = $("#zipcode").val();
  console.log(codeInput);
  console.log(zipcodeArray[0]);
  if (zipcodeArray.includes(codeInput)) {
    for (index = 0; index < cityArray.length; index++) {
      if (cityArray[index].code == codeInput) {
        $("#city_name").text(cityArray[index].name);
        $("#city_candidate").text(cityArray[index].candidat);
        $("#city_message").text(cityArray[index].message);
      }
    }

    //$("#city_name").text(Chartres.name);
    //$("#city_candidate").text(Chartres.candidat);
    //$("#city_message").text(Chartres.message);
  }
  else {
     $("#city_name").text("Connais pas");
     $("#city_candidate").text("Chais pas");
     $("#city_message").text("Rien à dire");
  }
}
