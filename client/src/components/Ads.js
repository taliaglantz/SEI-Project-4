import React from 'react'
import { Container, Grid, Image, Segment } from 'semantic-ui-react'

const Ads = () => {

  return (
    <Container >
      <Segment inverted color='blue' tertiary style={{ marginTop: '20px', marginBottom: '20px' }}>
        <h2 style={{ textAlign: 'center', textDecoration: 'underline', color: 'black', textShadow: '0px 0px 8px #ffffff', margin: '0px' }}>WINTER SALE NOW ON!</h2>
        <Grid container columns={3} style={{ marginTop: '1px', marginBottom: '1px' }}>
          <Grid.Column>
            <Image src='https://i.imgur.com/Vik8Spe.png' />
          </Grid.Column>
          <Grid.Column>
            <Image src='https://i.imgur.com/nhWk941.png' />
          </Grid.Column>
          <Grid.Column>
            <Image src='https://i.imgur.com/Xxa1Ykz.png' />
          </Grid.Column>
        </Grid>
      </Segment>
      
    </Container>
  )
}
export default Ads