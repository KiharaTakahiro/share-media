import React from "react";
import PrimaryButton from "../parts/buttons/primary_button"
import RequireText from "../parts/text_fields/nomal_text"
type Props = {}

const TopTemplate: React.FC<Props> = ({}) => (
  <div>
    <div>TOPページをのいろいろ</div>
    <PrimaryButton button_name="プライマリ"></PrimaryButton>
    <RequireText label="ユーザ名" />
  </div>
);

export default TopTemplate;