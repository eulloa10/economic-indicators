import NavBar from "../Navigation";
import Footer from "../Footer";
import DashboardContainer from "./DashboardContainer";

export default function Dashboard({ data }) {
  return (
    <>
      <NavBar />
      <DashboardContainer data={data} />
      <Footer />
    </>
  )
}

export const getStaticProps = async () => {
  console.log('ENTERED')
  const response = await fetch('http://localhost:8000/api/indicators/yield_curve');
  const data = await response.json();
  console.log('DATAPROPS :>> ', data);
  console.log('ENTERED')

  return {
    props: {
      data
    }
  }
}
