CLASSES = [
    'background', 'volcano', 'tree', 'skeleton', 'bird', 'person', 'river', 'eye', 'dragon', 'baby', 'fire', 'mountain', 'rose', 'flower', 'penis', 'bear', 'gun', 'bear', 'kangaroo', 'woman', 'tower', 'fox', 'lizard'
]


#CLASSES = [
#    'background', 'volcano', 'tree', 'skeleton', 'bird', 'person', 'river', 'eye', 'dragon', 'baby', 'fire', 'mountain', 'rose', 'flower', 'penis', 'bear', 'gun', 'kangaroo', 'woman', 'tower', 'fox', 'lizard'
#]

num_classes = len(CLASSES)

defs_en = {
    'volcano': "You will face an event that will make you angry or you will meet someone who is really mad.",
    'tree': "If you aren't already married, you will have a happy and long-lasting family. If you're married, you will have newcomers in your family.",
    'skeleton': "You're going to experience an event that will make you very upset. Your friends will be able to help with this. Make sure to treat them well.",
    'bird': "If you're waiting for news, you can be sure they will be positive. With the news you're waiting for, you might be able to accomplish nice things in your life. It could also be an event that will make you happy.",
    'person': "This is someone that is already in your circle, or a new person will enter your life. This person will be with you always, you will be good friends and you will be chasing new work opportunities together.",
    'river': "You're going through a troublesome period in your life. Seeing a river in your cup means that you will have a break from this soon. It may also be a cautionary sign.",
    'eye': "There are people who are jealous of you. These people are gossipping behind your back.",
    'dragon': "There are people around you who have plans to harm you.",
    'baby': "You or someone you know may learn that they are pregnant.",
    'fire': "You need to be careful with your next step. The negative consequences may harm you.",
    'mountain': "You will be promoted at work or your quality of life will improve.",
    'rose': "Good things will happen in your love life.",
    'flower': "You're going to have very nice things happen. You will be earning a lot of money or meeting the love of your life.",
    'penis': "You will get to work on something you love.",
    'bear': "It usually means that you have an enemy who's not the smartest. It may also mean that you're trapped in a relationship.",
    'gun': "It's a positive sign that you will make peace with your enemies.",
    'kangaroo': "You will have a good time with people you have just met or will meet.",
    'woman': "You will need to make important decisions. These decisions might be about marriage or work.",
    'tower': "You will be promoted at work very abruptly.",
    'fox': "You will receive news from someone that you like. These news will surprise you. This may also mean that your enemies are waiting for you to do wrong.",
    'lizard': "You are entering a period where not much will happen in your life, things are as usual."
}

defs_tr = {
    'volcano': {
        'tr': "volkan",
        'anlam': "Sinir ve stres manalarına gelir. Bu falın yorumu iki şekilde yapılır. Birincisi volkan sizin başınıza gelecek ve sinir olacağınız durumlar şeklindedir. İkincisi ise aşırı sinirli ve stresli kimseden bahsedilir. Usta falcılara göre falda volkan görmek, kişinin üzüleceği ve kederleneceği gelişmelere işarettir. Bu olaylar karşısında kişinin hazırlık yapma gibi bir durumu yoktur çünkü birden gelişecek ve hazırlıksız yakalayacaktır."
    },
    'tree': {
        'tr': "ağaç",
        'anlam': "Fal sahibi daha evlenmemiş ise mutlu ve yıllar boyu devam edecek bir aile kuracaktır. Kişi evli ise ailesine yeni üyeler katılacaktır."
    },
    'skeleton': {
        'tr': "iskelet",
        'anlam': "Fal sahibi, bu aralar yaşayacağı büyük üzüntü ve keder yüzünden dolayı perişan olacak. Bu durumdan ancak çevresindekilerin vereceği büyük destekle kurtulabilecek. Bu bağlamda fal baktıran kişi, arkadaşlarını hiçbir zaman ihmal etmemeli."
    },
    'bird': {
        'tr': "kuş",
        'anlam': "Eğer uzaklardan bir haber bekliyorsanız ve falınızda kuş çıkıyorsa size güzel haberler gelecektir. Bu haberle beraber hayatınızda çok güzel işler ortaya çıkabilir. Ayrıca haberci anlamının yanı sıra kuş aynı zamanda güzel ve mutluluk verici bir durumu da ifade eder."
    },
    'person': {
        'tr': "insan",
        'anlam': "Fal sahibinin etrafında bulunan kişileri ya da hayatına girecek yeni bir insanı simgelemektedir. Her daim yakınında yer alan bir kişi ile dostluklarının gelişeceğine ve onunla birlikte yeni iş fırsatları yakalayacaklarına delalet etmektedir."
    },
    'river': {
        'tr': "nehir",
        'anlam': "Kahve falı sahibinin yaşadığı problemli sürecein geçeceği anlamına gelir. Kahve falında nehir görmek, kimi zaman uyarı mahiyetinde olabilir."
    },
    'eye': {
        'tr': "göz",
        'anlam': "Fal sahibinin çevresinde onu kıskanan ve onun hakkında dedikodu yapan kişi veya kişilerin olduğunu gösterir."
    },
    'dragon': {
        'tr': "ejderha",
        'anlam': "Fal sahibinin etrafında olan ve ona kötü planlar yapan, pusu kuran kişileri işaret etmektedir."
    },
    'baby': {
        'tr': "bebek",
        'anlam': "Kişi eğer evli ise çok beklediği bebeğine kısa sürede kavuşacaktır. Evli değil bekarsa oldukça yakın çevresinden birinin doğum yapacağına delalet edilmektedir"
    },
    'fire': {
        'tr': "ateş",
        'anlam': "Kişi bundan sonra atacağı adımlarda daha dikkatli olmalıdır. Aksi halde olumsuzluklar ortaya çıkar ve fal sahibi bundan etkilenebilir."
    },
    'mountain': {
        'tr': "dağ",
        'anlam': "Kişinin makam ve mevkide yükseleceğine işaret etmektedir."
    },
    'rose': {
        'tr': "gül",
        'anlam': "Aşk hayatındaki olumlu işleri temsil eder."
    },
    'flower': {
        'tr': "çiçek",
        'anlam': "Fal sahibine inanılmaz mutluluklar yaşatacak olayların habercisidir",
    },
    'penis': {
        'tr': "penis",
        'anlam': "Sevilen bir işe ortak olunacağına, sıkıntılı günler geçireceğine, üzüntülerinin sona ereceğine ve hayatının geri kalanında şansının ve bahtının açık olacağına, kendisini mutlu eden tüm detayları hayatına katacağına alamettir."
        },
    'bear': {
        'tr': "ayı",
        'anlam': "Genellikle aptal bir düşmanı temsil eder. Başka fal uzmanlarına göre ise, herhangi bir kişinin esiri olmak ve onun boyunduruğu altına girmek anlamına gelir."
    },
    'gun': {
        'tr': "silah",
        'anlam': "Fal sahibinin düşmanları ile anlaşmaya varacağına işaret eden bu fal, hayırlı bir şekilde yorumlanmaktadır."
    },
    'kangaroo': {
        'tr': "kanguru",
        'anlam': "Fal sahibinin yaşantısında yeni insanlar ile tanışacağı ve onlarla keyifli bir vakit geçireceği yönünde delalet eder."
    },
    'woman': {
        'tr': "kadın",
        'anlam': "Falda kadın görmek önemli kararlar alınması anlamına gelmektedir. Bu fal önemli kararlar alınacağına ve kişinin hayatında önemli değişiklikler yaşanacağına dalalet etmektedir. Bu kararlar genellikle evlilik, iş değişikliği veya yeni eve taşınmak gibi kararlar olmaktadır."
    },
    'tower': {
        'tr': "kule",
        'anlam': "Fal sahibini iş hayatında bekleyen ani ve çok hızlı bir yükselişin habercisi olarak kabul edilir."
    },
    'fox': {
        'tr': "tilki",
        'anlam': "Kişi yakın bir zamanda sevdiği dostlarından haber alacaktır. Gelecek haberin beklenmeyen ve şaşırtıcı bir şekilde geleceği bilinmektedir. Falda tilki görmek sinsi düşmanların pusuda beklediğine yorulur."
    },
    'lizard': {
            'tr': "kertenkele",
            'anlam': "Kişinin, hareketsiz ve durgun bir döneme girdiğine işarettir."
    }
}
