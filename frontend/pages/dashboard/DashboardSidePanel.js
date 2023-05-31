import styles from '../../styles/Dashboard/DashboardSidePanel.module.css';

import MonthFilter from './MonthFilter';
import IndicatorFilter from './IndicatorFilter';

function DashboardSidePanel() {
  return (
    <div className={styles['dashboard-inner-container']}>
      <MonthFilter />
      <IndicatorFilter />
    </div>
  )
}

export default DashboardSidePanel;
