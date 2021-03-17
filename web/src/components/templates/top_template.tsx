import React from "react";
import PrimarySubmitButton from "../parts/buttons/primary_submit_button"
import RequireText from "../parts/text_fields/nomal_text"
type Props = {}

const TopTemplate: React.FC<Props> = () => (
  <div>
    <div>TOPページをのいろいろ</div>
    <PrimarySubmitButton button_name="プライマリ"/>
    <RequireText label="ユーザ名" />
  </div>
);

export default TopTemplate;