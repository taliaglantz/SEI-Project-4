# General Assembly Project 4: TKG Fashion

<img src="client/src/assets/Black & White Aesthetic Minimalist Signature Logo.png" alt="experience logo" width=300/>

## Table of Contents
- [Overview](#overview)
- [Brief](#brief)
- [Technologies used](#technologies-used)
- [Build](#build)
- [Known bugs](#known-bugs)
- [Wins and Challenges](#wins)
- [Future features](#future-features)
- [Key learnings](#key-learnings)

<a name="overview"></a>
## Overview
This project was my fourth and final project created during General Assembly’s Software Engineering Immersive Course, which I completed from September-December 2021.
<strong>The goal</strong>: As a group, build a full-stack application with a React front-end and a Django back-end.
TKG Fashion is an e-commerce website that allows users to browse through clothes from a range of sellers. Items can be filtered by certain categories and also displayed by random. If users are logged in, they are able to add items to their basket and also review items. 

### Timeframe
9 days

### Deployed link
https://tkg-fashion-site.herokuapp.com/ 

### Getting started and admin login
1. Either clone or download the source code.
2. From the root directory, run  `pipenv shell` then `python manage.py runserver` to get the back-end set up.
3. In a parallel terminal, run `cd client` then `yarn && yarn start` to get the front-end set up.


Please feel free to use the following login credentials:
- Email: talia@email.com
- Password: password2468

<img src="client/src/assets/Screenshot 2022-01-10 at 14.16.24.png" alt="homepage" />

<a name="brief"></a>
## Brief
Here is the brief we were given:
- We want a full stack application with a React front-end and a Django back-end
- We want to see a fully functional RESTful api with all CRUD routes (GET, POST, PUT, DELETE)
- We want you to use at least one OneToMany & one ManyToMany relationship (for solo projects, you just need one relationship)
- Custom authentication (register/login) is optional for solo projects, and a requirement for group projects.

<a name="technologies-used"></a>
## Technologies used

### Back-end:
- Python
- Django
- PostgreSQL
- Psycopg2-binary - postgreSQP library wrapper
- Pylint - python linter
- Autopep8 - python formatter
- Django REST framework
- Cloudinary for image uploads
- Pillow - python imaging library tool
- Pyjwt for authentication in python


### Front-end:
- React
- Axios
- React Semantic UI (CSS Framework)
- Animate css
- Pure-react-carousel for carousel
- React-router-dom for component-based routing


### Dev tools:
- VS code
- Yarn
- Insomnia
- TablePlus
- Google Chrome dev tools
- Heroku for deployment
- Asana for planning and timeline
- Google Jamboard for wireframing
- LucidChart for Entity Relationship Diagram (ERD)

<a name="build"></a>
## Build

### Planning
We were given the option to do this project solo however two of my fellow peers (friends I’d say at this point) and I were put together in a workshop for the first time and discovered how similar we were and how well we worked together. We all loved working in teams so we decided to work as a group for our final project, we later found out that we were the only group on the whole course! 
None of us had done an e-commerce website before and we all wanted to give it a go. As soon as we came up with our idea and before we went any further, we had a discussion where we processed our last group projects - the dynamics, what worked well, what didn’t etc. - and set an environment for how we’d all like this project to go. The main points we took from this were:
1. KISS - simple and effective, for the win!
2. Communication is key
3. Stick to plan and timings

We then moved onto looking at our relationships. Given we were a group, we knew we needed a few different relationships in order to fulfil the brief. We decided we wanted there to be a many-to-many relationship between the sellers and products and a one-to-many relationship between the product and reviews. We then factored in the orders and images used for the products and drew relationships accordingly.

<img src="client/src/assets/ERD for TKG Fashion.png" alt="ERD" />

We then set out to design our wireframe. We had a look at a few popular e-commerce websites and based our design and layout on those, remembering that the simpler the better! For our wireframes, we used Google Jamboard. I had never used this tool before so enjoyed learning about yet another wireframing site.

<img src="client/src/assets/Wireframe - Project 4 1.png" alt="Wireframe - homepage" width=300/>
<img src="client/src/assets/Wireframe - Project 4 3.png" alt="Wireframe - login/register" width=300/>
<img src="client/src/assets/Wireframe - Project 4 4.png" alt="Wireframe - index" width=300/>
<img src="client/src/assets/Wireframe - Project 4 5.png" alt="Wireframe - showpage" width=300/>
<img src="client/src/assets/Wireframe - Project 4 6.png" alt="Wireframe - similar items" width=300/>
<img src="client/src/assets/Wireframe - Project 4 7.png" alt="Wireframe - bag" width=300/>

Finally, we compartmentalised our tasks on Asana and ensured we managed our time correctly by having a distinct “stretch goals” section. This section would only be touched when the MVP had been reached. Every morning and late afternoon we looked at the Asana board and assessed our progress, we also discussed our current tasks and talked through potential blockers. We used Git and GitHub for version control and always did our pushes and pulls together to avoid conflict flare-ups. 

<img src="client/src/assets/Screenshot 2022-01-10 at 14.25.22.png" alt="Wireframe - bag"/>

Key dates:
- Day 1: Planning
- Day 7: MVP
- Day 8: Bonus tasks
- Day 9: Styling

## Days 2-4: Back-end
As we all had only a week’s experience each with both Django and Python, we decided to build the back-end together so we could all go over our notes and work through problems as a group. 
Although it was tricky at times, I really liked how clear Django’s error messaging was and so this helped us out a lot.
We built 6 models in total, with views and serialisers (some populated), by using Django and Django REST framework to create a PostgreSQL database with RESTful features. We used TablePlus to visualise our database and Insomnia to check our requests, constantly making sure we were getting back the correct JSON messages in response. 
Half way through day 4, we split up and whilst my team members were learning about and implementing the seeding process, I was doing the same for our custom user model and the signup and login authentication. I started off by building the jwt_auth app with the model, then gradually adding in the `JWTAuthentication`, `UserSerializer` and `PopulatedUserSerializer`, then `RegisterView` and `LoginView`.
```
class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
```

## Day 4-6: ProductShow and SimilarProducts
The component that I took ownership of was ProductShow and consequently SimilarProducts. Pulling the data through for the details of the items was relatively straightforward and I’m really pleased how the colour of the items is displayed.

<img src="client/src/assets/Screenshot 2022-01-10 at 15.09.51.png" alt="Show page"/>

I had also never built an accordion before and thought this was a really nice stylistic touch that adds a lot of character to the page. 
Another group member wrote the code for the review form however we combined the components and code together. 
The similar products segment is imported into the product show component, and the items that are displayed are only those that are within the category of the item on the page. 
```
const filterByCategory = () => {

    return allProducts.filter(product => {
      return product.category === category
    })
  }
```
You’ll also notice that there is a ternary in place of what should be a simple url for the src. This happened on a few occasions in project 3 as well as in project 4 so the ternary is what we came up with as a solution and it seems to work well.
```
<Image src={product.image_set !== undefined ? product.image_set[0].image : null} />
``` 

## Day 7 and 8: Login and Register, Filtering on product index and Bag
Both the register and logins are built by making axios POST requests, and the login uses local storage for the token. We knew we wanted the login and register forms to appear as modals however initially it was a challenge to build them using React Semantic UI and it took some googling of solutions before we figured out how to do it.
```
const setItemToLocalStorage = (token) => {
    window.localStorage.setItem('token', token)
  }

  const handleSubmit = async event => {
    event.preventDefault()
    try {
      const { data } = await axios.post('/api/auth/login/', formData)
      setItemToLocalStorage(data.token)
      navigate('/browse')
    } catch (err) {
      setError(true)
    }
  }
```

<img src="client/src/assets/Screenshot 2022-01-10 at 15.32.42.png" alt="Show page" width=400 />
<img src="client/src/assets/Screenshot 2022-01-10 at 15.32.28.png" alt="Show page" width=400 />

Although it was another group member that took the lead on building the filters, I had never had hands on experience with this before so wanted to help out and understand them. I worked on the gender filter (given more time I would have looked at this again and perhaps created a unisex/all category too).

```
const genderOptions = [
  { key: 1, text: 'Male', value: 'M', icon: 'male' },
  { key: 2, text: 'Female', value: 'F', icon: 'female' }
]

const [genderValue, setGenderValue] = React.useState(null)

const filteredProducts = products.filter(product => {
    return (
      (product.category === categoryValue || categoryValue === null) && // we can filter out for our category
      (product.gender === genderValue || genderValue === null) // and gender options in one go
    )
  }).sort((a, b) => { // chaining on our sorting function at the end of filter
    if (priceValue === null) return 0 // If no price filter set dont sort
    if (priceValue === 1) return a.price - b.price // low to high
    if (priceValue === 2) return b.price - a.price // high to low
  })
```
The Bag we left relatively late for such a crucial (arguably the most crucial) component, however we wanted to work on it together. We had to work a bit on the backend initially to ensure that we could pull the products details through to the orders, we did this by ensuring the populated product serialiser and the order model was set up correctly.
```
class Order(models.Model):
    customer = models.ForeignKey('jwt_auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
```
```
class PopulatedOrderSerializer(OrderSerializer):
    product = PopulatedProductSerializer(read_only=True)
```
We created the logic to ensure that the only items that are displayed in the basket are those that the customer who is currently logged in has added to their bag. The customer can only add items to their bag if they are signed in.

<img src="client/src/assets/Screenshot 2022-01-10 at 15.47.31.png" alt="Bag" />

## Day 9: Styling, seeding, responsiveness
We did a lot of the styling as we went along, however towards the end of the project we officially agreed on a colour scheme and built in the animations. Since it was a few weeks before Christmas, we went for a cooler theme with some winter magic in the sale segment on the homepage.
The seeding we did as we went along however we each took a section to populate - I added in all the reviews and users. 
Making the site responsive was the last task we completed, hence why it is a little glitchy at points, however we are glad we managed to add in this feature.

<a name="known-bugs"></a>
## Known bugs
- The filtering works well however it’s quite temperamental and doesn’t really like it if you want to clear the filter
- The site can generally be classified as mobile-responsive however sometimes it’s a bit glitchy and not everything appears in proportion.
- We couldn’t get the success or fail messages to show up when a user has signed up, telling them to log in - so the user has to be specifically told (here goes!) that if you signup and the modal disappears, you are successful and you need to log in, otherwise, you need to keep trying to sign up! 

<a name="wins"></a>
## Wins
- We definitely used a sufficient number of relationships and I enjoyed seeing how using them creates the flow in the back-end which makes it easier to piece together the front-end
- Although a friend worked on the clothing filters on the home page and the carousels, this was all new to me and I enjoyed learning about how they were built - every new piece of learning is definitely a win for me!
- I hadn’t had the time in any of my projects to make my apps fully responsive so I’m really glad that we managed to make this one as so.
- I think we managed our time well and worked efficiently together, so it was no surprise to me how we managed to get a lot of our stretch goals accomplished - filtering by more than one category, random card generator, similar items and responsiveness. We also managed to really fine-tune the styling at the end  - this is particularly noticeable in the fun animations we added into each page.
- I think we’ve got good error handling and it makes the flow of the app look smooth.

<a name="challenges"></a>
## Challenges
- Having only had a week of both learning and practising Django and Python, and some interruptions during our course, getting to grips with a new language and implementing the back-end was a real challenge. I found getting to grips with the populated serialisers particularly tricky, however we had lots of practice with this in our project, for example when we wanted the user’s username to appear when they left a review and the product information in the orders, and I now feel much more comfortable with them. We took a calm and collected approach to building the back-end - constantly referring to our notes, reading Django docs and testing everything out in Insomnia and TablePlus - and I’m really proud of what we achieved.

<a name="future-features"></a>
## Future features
- Had a christmas section in our original plan but that turned into a stretch goal.
- We were trying on the last day or so to add in a “checkout”/payment feature however didn’t want to rush it. Without the payment feature, we felt the app could definitely still be classified as e-commerce!
- The favouriting of items to form a wishlist.
- Better error handling for signup and login - Python has its own error handling but only the back-end can see that - it should be brought to the front to help the user.

<a name="key-learnings"></a>
## Key learnings
- I am really proud of the app that we created and think a really big win is how we made an app that looks slick, detailed and professional out of some relatively straightforward ideas whilst sticking to simple and basic principles. Our initial processing of previous projects was crucial to our workflow and the clear goals and intricate planning we did gave us clear boundaries. Our communication was also clear and always ongoing which made the transitions between tasks seamless and relatively obstacle-free! These are all invaluable experiences and learnings that I will be taking forward into my new career. 
- A really important win for me too was that this project was so much fun to create, I thoroughly enjoyed all the work I did and truly felt that all the knowledge I gained and soft-skills I learnt and developed leading up to this point, really allowed me to thrive and love every minute of producing this project. I know that enjoying what you are doing is paramount to success and this project was pure proof of this.